#!/usr/bin/env bash
# ==============================================================================
# Hermes Agent Enterprise AI Ecosystem Platform & Vault Installer
# Sovereign Multi-User Environment & Hybrid Vector Registry
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
HERMES_USER="${HERMES_USER:-hermes}"
VALIDATE_ONLY=0

show_help() {
    cat <<'HELP'
Hermes Agent Enterprise AI Ecosystem Platform Installer

Usage:
  sudo bash install.sh [options]

Options:
  --user <account>     Target service user for isolated environment (default: hermes)
  --validate-only      Run health audit and testbench without modifying system
  -h, --help           Show this help message

Environment Variables:
  HERMES_USER          Override default isolated service user (default: hermes)
  HERMES_HOME          Explicit path for Hermes home (.hermes)
HELP
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --user)
            [[ $# -ge 2 ]] || { echo "ERROR: --user requires a username" >&2; exit 2; }
            HERMES_USER="$2"
            shift 2
            ;;
        --validate-only)
            VALIDATE_ONLY=1
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
echo "  Execution Mode        : $( [[ $VALIDATE_ONLY -eq 1 ]] && echo 'Validation Audit' || echo 'Production Deployment' )"
echo "  Workspace Root        : ${SCRIPT_DIR}"
echo "=============================================================================="

# Delegate to local installer with configured parameters
if [[ $EUID == 0 ]]; then
    exec bash "${SCRIPT_DIR}/install-hermes-local.sh" --user "${HERMES_USER}" $( [[ $VALIDATE_ONLY -eq 1 ]] && echo '--validate-only' )
else
    echo "[!] Non-root execution detected. Elevating via sudo to configure system user '${HERMES_USER}'..."
    exec sudo bash "${SCRIPT_DIR}/install-hermes-local.sh" --user "${HERMES_USER}" $( [[ $VALIDATE_ONLY -eq 1 ]] && echo '--validate-only' )
fi
