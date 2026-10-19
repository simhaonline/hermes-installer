#!/usr/bin/env bash
# ==============================================================================
# Hermes Agent Enterprise AI Ecosystem Platform & Vault Installer
# Sovereign Multi-User Environment & Hybrid Vector Registry
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
HERMES_USER="${HERMES_USER:-hermes}"
VALIDATE_ONLY=0
DO_UPDATE=0
INSTALL_CRON=0
CRON_SCHEDULE="0 3 * * *"
REMOVE_CRON=0
ALL_USERS=0

show_help() {
    cat <<'HELP'
Hermes Agent Enterprise AI Ecosystem Platform & Vault Installer

Usage:
  sudo bash install.sh [options]

Options:
  --update                Incrementally update Prompts, Skills, Agents, MCPs, and Plugins
  --all-users             Synchronize vault across all system users with isolated .hermes environments
  --install-cron [sched]  Install automated periodic sync cron job (default: "0 3 * * *")
  --remove-cron           Remove automated sync cron job
  --user <account>        Target service user for isolated environment (default: hermes)
  --validate-only         Run health audit and testbench without modifying system
  -h, --help              Show this help message

Environment Variables:
  HERMES_USER             Override default isolated service user (default: hermes)
  HERMES_HOME             Explicit path for Hermes home (.hermes)
HELP
}

PASS_ARGS=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --update)
            DO_UPDATE=1
            PASS_ARGS+=("--update")
            shift
            ;;
        --all-users)
            ALL_USERS=1
            PASS_ARGS+=("--all-users")
            shift
            ;;
        --install-cron)
            INSTALL_CRON=1
            if [[ $# -ge 2 && "$2" != --* ]]; then
                CRON_SCHEDULE="$2"
                PASS_ARGS+=("--install-cron" "$2")
                shift 2
            else
                PASS_ARGS+=("--install-cron")
                shift
            fi
            ;;
        --remove-cron)
            REMOVE_CRON=1
            PASS_ARGS+=("--remove-cron")
            shift
            ;;
        --user)
            [[ $# -ge 2 ]] || { echo "ERROR: --user requires a username" >&2; exit 2; }
            HERMES_USER="$2"
            PASS_ARGS+=("--user" "$2")
            shift 2
            ;;
        --validate-only)
            VALIDATE_ONLY=1
            PASS_ARGS+=("--validate-only")
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo "ERROR: Unknown option: $1" >&2
            show_help >&2
            exit 2
            ;;
    esac
done

echo "=============================================================================="
echo "    Hermes Agent Enterprise AI Ecosystem Platform & Vault Installer           "
echo "=============================================================================="
echo "  Target Dedicated User : ${HERMES_USER}"
echo "  Execution Mode        : $( [[ $VALIDATE_ONLY -eq 1 ]] && echo 'Validation Audit' || ( [[ $DO_UPDATE -eq 1 ]] && echo 'Incremental Update' || echo 'Production Deployment' ) )"
echo "  Workspace Root        : ${SCRIPT_DIR}"
echo "=============================================================================="

# Delegate to local installer with configured parameters
if [[ $EUID == 0 || $VALIDATE_ONLY -eq 1 || $DO_UPDATE -eq 1 ]]; then
    exec bash "${SCRIPT_DIR}/install-hermes-local.sh" "${PASS_ARGS[@]}"
else
    echo "[!] Non-root execution detected. Elevating via sudo to execute full installation..."
    exec sudo bash "${SCRIPT_DIR}/install-hermes-local.sh" "${PASS_ARGS[@]}"
fi
