#!/usr/bin/env bash
set -euo pipefail

echo "======================================================================"
echo "    Hermes Agent Enterprise Offline Installer Bootstrap"
echo "======================================================================"
TAG="${HERMES_INSTALLER_TAG:-v1.0.0}"
URL="https://github.com/simhaonline/hermes-installer/releases/download/${TAG}/hermes-self-contained-installer.tar.gz"
ARCHIVE="hermes-self-contained-installer.tar.gz"

echo "[1/3] Downloading installer package from GitHub Releases (${TAG})..."
if command -v curl >/dev/null 2>&1; then
    curl -fL# -o "$ARCHIVE" "$URL"
elif command -v wget >/dev/null 2>&1; then
    wget --progress=bar:force -O "$ARCHIVE" "$URL"
else
    echo "ERROR: curl or wget is required." >&2
    exit 1
fi

echo "[2/3] Extracting installer package..."
tar -xzf "$ARCHIVE"
cd hermes-self-contained-installer

echo "[3/3] Executing local offline installer..."
sudo bash install-hermes-local.sh "$@"
