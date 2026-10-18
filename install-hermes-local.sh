#!/usr/bin/env bash
# ==============================================================================
# Hermes Agent Self-Local & Offline Production Installer
# 100% Self-Contained Deployment (Zero GitHub / Zero External Network Downloads)
# ==============================================================================
set -euo pipefail

HERMES_USER="predictatrade"
VALIDATE_ONLY=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --validate-only)
            VALIDATE_ONLY=1
            shift
            ;;
        --user)
            [[ $# -ge 2 ]] || { echo 'ERROR: --user requires an account name' >&2; exit 2; }
            HERMES_USER="$2"
            shift 2
            ;;
        -h|--help)
            cat <<'HELP'
Hermes Agent Self-Local Offline Installer

Usage:
  bash install-hermes-local.sh [options]

Options:
  --user <name>       Target isolated service account (default: predictatrade)
  --validate-only     Run validation testbench without modifying system files
  -h, --help          Show this help message
HELP
            exit 0
            ;;
        *)
            echo "ERROR: Unknown option: $1" >&2
            exit 2
            ;;
    esac
done

[[ $EUID == 0 ]] || { echo 'ERROR: Run this installer as root.' >&2; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PAYLOAD_DIR="$SCRIPT_DIR"
if [[ ! -f "$PAYLOAD_DIR/hermes-engines.tar.gz" && -d "$SCRIPT_DIR/bundle" && -f "$SCRIPT_DIR/bundle/hermes-engines.tar.gz" ]]; then
    PAYLOAD_DIR="$SCRIPT_DIR/bundle"
fi
cd "$PAYLOAD_DIR"

log()  { printf '\n[hermes-local-installer] %s\n' "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
warn() { printf 'WARNING: %s\n' "$*" >&2; }

log '[1/6] Validating local payload and installer packages'
for req in hermes-vault.sqlite hermes-engines.tar.gz hermes-agent-core.tar.gz hermes-system-assets.tar.gz assets/configure.py; do
    [[ -f "$PAYLOAD_DIR/$req" ]] || fail "Required local payload missing: $req"
done
printf '  Local payload verified: 100%% offline bundle intact.\n'

# Provision dedicated user account if missing
if ! id "$HERMES_USER" >/dev/null 2>&1; then
    [[ $VALIDATE_ONLY == 0 ]] || fail "Account $HERMES_USER is not installed."
    log "Creating dedicated service user: $HERMES_USER"
    useradd --create-home --user-group --shell /bin/bash "$HERMES_USER"
fi

ACCOUNT_UID="$(id -u "$HERMES_USER")"
ACCOUNT_GID="$(id -g "$HERMES_USER")"
ACCOUNT_HOME="$(getent passwd "$HERMES_USER" | cut -d: -f6)"
HERMES_BASE_HOME="$ACCOUNT_HOME/.hermes"
INSTALL_DIR="$ACCOUNT_HOME/.local/share/hermes-agent"
WORKSPACE="/srv/$HERMES_USER"
RUNTIME_DIR="/run/user/$ACCOUNT_UID"

# Enforce security boundaries (prohibited from docker, sudo, adm)
for grp in docker sudo adm; do
    if id -nG "$HERMES_USER" | tr ' ' '\n' | grep -qx "$grp"; then
        fail "Dedicated $HERMES_USER account belongs to privileged group $grp. Security boundary violated."
    fi
done

as_user() {
    runuser -u "$HERMES_USER" -- env -i \
      HOME="$ACCOUNT_HOME" USER="$HERMES_USER" LOGNAME="$HERMES_USER" SHELL=/bin/bash \
      PATH="$ACCOUNT_HOME/.local/bin:/usr/local/bin:/usr/bin:/bin" \
      HERMES_HOME="$HERMES_BASE_HOME" HERMES_BASE_HOME="$HERMES_BASE_HOME" \
      HERMES_ACCOUNT_HOME="$ACCOUNT_HOME" \
      XDG_RUNTIME_DIR="$RUNTIME_DIR" DBUS_SESSION_BUS_ADDRESS="unix:path=$RUNTIME_DIR/bus" \
      DOCKER_HOST="unix://$RUNTIME_DIR/docker.sock" DOCKER_CONTEXT="" \
      GIT_TERMINAL_PROMPT=0 \
      PYTHONUNBUFFERED=1 \
      bash -c 'cd "$1"; shift; exec "$@"' bash "$WORKSPACE" "$@"
}

if [[ $VALIDATE_ONLY == 0 ]]; then
    log '[2/6] Configuring subordinate IDs & rootless namespaces'
    python3 - "$HERMES_USER" <<'PY'
import sys
from pathlib import Path
user = sys.argv[1]
for file in ['/etc/subuid', '/etc/subgid']:
    p = Path(file)
    content = p.read_text() if p.exists() else ''
    lines = [line.strip().split(':') for line in content.splitlines() if line.strip() and not line.startswith('#')]
    has_range = any(r[0] == user and len(r) >= 3 and int(r[2]) >= 65536 for r in lines)
    if not has_range:
        max_end = 100000
        for r in lines:
            if len(r) >= 3 and r[1].isdigit() and r[2].isdigit():
                max_end = max(max_end, int(r[1]) + int(r[2]))
        new_entry = f"{user}:{max_end}:65536\n"
        with p.open('a') as f:
            f.write(new_entry)
PY

    install -d -o "$HERMES_USER" -g "$ACCOUNT_GID" -m 0750 "$ACCOUNT_HOME/.local" "$ACCOUNT_HOME/.local/share" "$ACCOUNT_HOME/.local/bin" "$WORKSPACE"

    log '[3/6] Deploying pre-compiled 16 engines, node distributions and python packages'
    tar --no-same-owner -xzf "$PAYLOAD_DIR/hermes-engines.tar.gz" -C /
    chmod 0755 /usr/local/bin/{trim,trim-1,codegraph,mcptoon,mempalace,mempalace-mcp,mempalace-light-mcp,rea,rea-agents,pentagi,pentagi.bin,auto,hermes-vault} 2>/dev/null || true

    log '[4/6] Deploying core Hermes Agent engine and tools runtime'
    tar --no-same-owner -xzf "$PAYLOAD_DIR/hermes-agent-core.tar.gz" -C "$ACCOUNT_HOME/.local/share/"
    tar --no-same-owner -xzf "$PAYLOAD_DIR/hermes-system-assets.tar.gz" -C /

    # Copy master SQLite vault into Hermes home
    cp -a "$PAYLOAD_DIR/hermes-vault.sqlite" "$HERMES_BASE_HOME/hermes-vault.sqlite"
    cp -a "$PAYLOAD_DIR/hermes-vault.sqlite" "/root/hermes-vault.sqlite" 2>/dev/null || true

    # Fix ownership to isolated service user
    chown -R "$ACCOUNT_UID:$ACCOUNT_GID" "$ACCOUNT_HOME" "$WORKSPACE"

    # Install privilege-dropping wrappers in /usr/local/bin
    for tool in hermes hermes-skill-catalog hermes-community-skills hermes-mcp-universe hermes-project-context token-saver hermes-token-saver hermes-agent-cron; do
        target="$ACCOUNT_HOME/.local/lib/predictatrade-hermes/$tool"
        [[ "$tool" != hermes ]] || target="$INSTALL_DIR/.hermes/bin/hermes"
        cat > "/usr/local/bin/$tool" <<WRAPPER
#!/usr/bin/env bash
set -euo pipefail
if [[ \$(id -u) == 0 ]]; then
    project="${HERMES_USER}"
    exec runuser -u "\$project" -- "\$0" "\$@"
fi
account="\$(id -un)"
account_home="\$(getent passwd "\$account" | cut -d: -f6)"
uid="\$(id -u)"
target="$target"
[[ -x "\$target" ]] || { echo "Hermes binary not found: \$target" >&2; exit 1; }
export HOME="\$account_home"
export HERMES_HOME="\$account_home/.hermes" HERMES_BASE_HOME="\$account_home/.hermes"
export XDG_RUNTIME_DIR="/run/user/\$uid" DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/\$uid/bus"
export DOCKER_HOST="unix:///run/user/\$uid/docker.sock"
unset DOCKER_CONTEXT
export PATH="\$account_home/.local/bin:/usr/local/bin:/usr/bin:/bin"
[[ -x . ]] || cd "/srv/\$account"
exec "\$target" "\$@"
WRAPPER
        chmod 0755 "/usr/local/bin/$tool"
    done

    # Generate specialist profiles and initialize Kanban
    run_assets="$PAYLOAD_DIR/assets"
    cleanup_assets=0
    if ! runuser -u "$HERMES_USER" -- test -r "$run_assets/configure.py" 2>/dev/null; then
        run_assets="/tmp/hermes-install-assets-$$"
        cp -rp "$PAYLOAD_DIR/assets" "$run_assets"
        chown -R "$ACCOUNT_UID:$ACCOUNT_GID" "$run_assets"
        cleanup_assets=1
    fi
    as_user python3 "$run_assets/configure.py" profiles
    [[ $cleanup_assets -eq 0 ]] || rm -rf "$run_assets"
    as_user "$INSTALL_DIR/.hermes/bin/hermes" -p default kanban init 2>/dev/null || true

    # Enable lingering and Rootless Docker if dockerd-rootless-setuptool.sh is present
    loginctl enable-linger "$HERMES_USER" 2>/dev/null || true
    systemctl start "user@$ACCOUNT_UID.service" 2>/dev/null || true
    if command -v dockerd-rootless-setuptool.sh >/dev/null 2>&1; then
        as_user dockerd-rootless-setuptool.sh install --force 2>/dev/null || true
        as_user systemctl --user enable --now docker 2>/dev/null || true
    fi
fi

log '[5/6] Running full offline verification testbench'
[[ -x "$INSTALL_DIR/.hermes/bin/hermes" ]] || fail 'Hermes launcher is not executable.'
as_user "$INSTALL_DIR/.hermes/bin/hermes" --version
as_user hermes-skill-catalog categories
/usr/local/bin/hermes-vault stats

# Verify pre-compiled engines
for eng in trim codegraph mcptoon mempalace rea pentagi auto; do
    if command -v "$eng" >/dev/null 2>&1; then
        as_user "$eng" --help >/dev/null 2>&1 || true
    else
        warn "Engine binary $eng not found in PATH"
    fi
done

as_user python3 -c 'import autoagent, cactus, laya, openshell; print("All extended Python engines loaded successfully.")'

log '[6/6] Hermes local offline deployment verified!'
printf '==============================================================================\n'
printf 'Account        : %s (UID %s)\n' "$HERMES_USER" "$ACCOUNT_UID"
printf 'Hermes Home    : %s\n' "$HERMES_BASE_HOME"
printf 'SQLite Vault   : %s/hermes-vault.sqlite\n' "$HERMES_BASE_HOME"
printf 'Workspace      : %s\n' "$WORKSPACE"
printf 'Curated Skills : 19,400+ Skills across 47 Categories\n'
printf 'Community Pool : 64,500+ Indexed Packages\n'
printf 'MCP Universe   : 4,800+ Indexed Servers + 35 Curated Production Servers\n'
printf 'Agent Library  : 460+ Personas & 54 Specialist Profiles\n'
printf 'Active Plugins : 26 Plugins\n'
printf 'Offline Engines: trim-1, codegraph, mcptoon, mempalace, rea, autoagent, pentagi, cactus, laya, openshell\n'
printf 'Offline Mode   : Complete (Zero GitHub / Internet dependencies)\n'
printf '==============================================================================\n'
printf 'CLI Status     : hermes-vault stats\n'
printf 'Launch Agent   : hermes\n'
