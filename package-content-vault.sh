#!/usr/bin/env bash
# ==============================================================================
# Hermes Agent Pure Content Vault Packager (Option A - Lightweight Release)
# Builds zero-binary, content-only archive for fast deployment & backup.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
DIST_DIR="$SCRIPT_DIR/dist"
ARCHIVE_NAME="hermes-content-vault-v1.1.0.tar.gz"
TARGET_ARCHIVE="$DIST_DIR/$ARCHIVE_NAME"

mkdir -p "$DIST_DIR"

echo "=============================================================================="
echo "    Packaging Hermes Pure Content Vault (Option A: Lightweight Release)       "
echo "=============================================================================="

DB_SOURCE="/home/predictatrade/.hermes/hermes-vault.sqlite"
if [[ ! -f "$DB_SOURCE" ]]; then
    DB_SOURCE="$SCRIPT_DIR/hermes-vault.sqlite"
fi

if [[ ! -f "$DB_SOURCE" ]]; then
    echo "ERROR: hermes-vault.sqlite not found at $DB_SOURCE" >&2
    exit 1
fi

STAGE_DIR="$(mktemp -d /tmp/hermes-vault-stage-XXXXXX)"
trap 'rm -rf "$STAGE_DIR"' EXIT

echo "[1/4] Copying and verifying SQLite database..."
cp -p "$DB_SOURCE" "$STAGE_DIR/hermes-vault.sqlite"

# Verify SQLite integrity
sqlite3 "$STAGE_DIR/hermes-vault.sqlite" "PRAGMA integrity_check;" | grep -q "ok" || {
    echo "ERROR: SQLite integrity check failed!" >&2
    exit 1
}

echo "[2/4] Staging CLI tools and collection manifests..."
cp -p "$SCRIPT_DIR/hermes-vault" "$STAGE_DIR/"
cp -p "$SCRIPT_DIR/hermes-registry" "$STAGE_DIR/" 2>/dev/null || true
cp -p "$SCRIPT_DIR/install-hermes-local.sh" "$STAGE_DIR/"
cp -p "$SCRIPT_DIR/README-LOCAL-INSTALL.md" "$STAGE_DIR/"
cp -p "$SCRIPT_DIR/README-HERMES.md" "$STAGE_DIR/"

mkdir -p "$STAGE_DIR/assets"
cp -rp "$SCRIPT_DIR/assets/collection-manifest.json" "$STAGE_DIR/assets/"
cp -rp "$SCRIPT_DIR/assets/profiles.json" "$STAGE_DIR/assets/"
cp -rp "$SCRIPT_DIR/assets/recommended-mcp-servers.json" "$STAGE_DIR/assets/"
cp -rp "$SCRIPT_DIR/assets/configure.py" "$STAGE_DIR/assets/"

CHROMA_SOURCE="/home/predictatrade/.hermes/vector-registry"
if [[ -d "$CHROMA_SOURCE" ]]; then
    echo "  -> Staging ChromaDB vector registry embeddings..."
    cp -rp "$CHROMA_SOURCE" "$STAGE_DIR/vector-registry"
fi

echo "[3/4] Compressing into lightweight content archive..."
tar -czf "$TARGET_ARCHIVE" -C "$STAGE_DIR" .

ARCHIVE_SIZE="$(du -h "$TARGET_ARCHIVE" | cut -f1)"
ARCHIVE_SHA="$(sha256sum "$TARGET_ARCHIVE" | cut -d' ' -f1)"

echo "[4/4] Updating SHA256SUMS.txt..."
sed -i "/$ARCHIVE_NAME/d" "$SCRIPT_DIR/SHA256SUMS.txt" 2>/dev/null || true
printf '%s  %s\n' "$ARCHIVE_SHA" "$ARCHIVE_NAME" >> "$SCRIPT_DIR/SHA256SUMS.txt"

# Update vault hash as well
DB_SHA="$(sha256sum "$DB_SOURCE" | cut -d' ' -f1)"
sed -i "/hermes-vault.sqlite/d" "$SCRIPT_DIR/SHA256SUMS.txt" 2>/dev/null || true
printf '%s  hermes-vault.sqlite\n' "$DB_SHA" >> "$SCRIPT_DIR/SHA256SUMS.txt"
# Ensure ownership remains hermes-installer:hermes-installer
chown -R hermes-installer:hermes-installer "$DIST_DIR" "$SCRIPT_DIR/SHA256SUMS.txt" 2>/dev/null || true

echo "=============================================================================="
echo "Content Archive : $TARGET_ARCHIVE"
echo "Archive Size    : $ARCHIVE_SIZE"
echo "SHA-256 Checksum: $ARCHIVE_SHA"
echo "SQLite Vault    : $DB_SHA"
echo "Status          : Packaged successfully with zero binary bloat."
echo "=============================================================================="
