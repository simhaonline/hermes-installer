#!/usr/bin/env bash
# ==============================================================================
# Hermes Agent Enterprise Hybrid Vector Registry & Platform Bootstrap
# 1-Line Bootstrap Installer from GitHub Releases (Option A: Lightweight Vault)
# ==============================================================================
set -euo pipefail

echo "======================================================================"
echo "    Hermes Agent Enterprise Hybrid Vector Registry Bootstrap"
echo "======================================================================"

TAG="${HERMES_INSTALLER_TAG:-v1.0.0}"
REPO="simhaonline/hermes-installer"
BASE_URL="https://github.com/${REPO}/releases/download/${TAG}"
ARCHIVE="hermes-content-vault-${TAG}.tar.gz"
CHECKSUM_FILE="SHA256SUMS.txt"
TMP_DIR="$(mktemp -d /tmp/hermes-quick-install-XXXXXX)"

trap 'rm -rf "$TMP_DIR"' EXIT

echo "[1/4] Downloading lightweight Content Vault & Vector Registry (${TAG})..."
fetch() {
    local url="$1"
    local dest="$2"
    if command -v curl >/dev/null 2>&1; then
        curl -fL# -o "$dest" "$url"
    elif command -v wget >/dev/null 2>&1; then
        wget --progress=bar:force -O "$dest" "$url"
    else
        echo "ERROR: curl or wget is required." >&2
        exit 1
    fi
}

fetch "${BASE_URL}/${ARCHIVE}" "${TMP_DIR}/${ARCHIVE}"
fetch "${BASE_URL}/${CHECKSUM_FILE}" "${TMP_DIR}/${CHECKSUM_FILE}"

echo "[2/4] Verifying cryptographic integrity..."
cd "$TMP_DIR"
EXPECTED_SHA="$(grep "$ARCHIVE" "$CHECKSUM_FILE" | awk '{print $1}')"
if [[ -n "$EXPECTED_SHA" ]]; then
    ACTUAL_SHA="$(sha256sum "$ARCHIVE" | awk '{print $1}')"
    if [[ "$EXPECTED_SHA" != "$ACTUAL_SHA" ]]; then
        echo "ERROR: Checksum mismatch for $ARCHIVE!" >&2
        echo "  Expected: $EXPECTED_SHA" >&2
        echo "  Actual  : $ACTUAL_SHA" >&2
        exit 1
    fi
    echo "  Cryptographic checksum verified: SHA256 match ($ACTUAL_SHA)"
fi

echo "[3/4] Extracting package..."
STAGE_DIR="$TMP_DIR/extracted"
mkdir -p "$STAGE_DIR"
tar -xzf "$ARCHIVE" -C "$STAGE_DIR"
cd "$STAGE_DIR"

echo "[4/4] Executing Hermes local production deployment..."
if [[ $EUID == 0 ]]; then
    bash install.sh "$@"
else
    sudo bash install.sh "$@"
fi

echo "======================================================================"
echo "  🎉 Hermes Agent Platform & Hybrid Registry Installed Successfully!"
echo "======================================================================"
echo "  • CLI Hybrid Search : hermes-registry resolve \"<intent>\""
echo "  • CLI Ecosystem DB  : hermes-vault stats"
echo "  • Interactive Web UI: http://localhost:8998 (or hermes-registry ui)"
echo "  • Service Daemon    : sudo systemctl status hermes-registry"
echo "======================================================================"
