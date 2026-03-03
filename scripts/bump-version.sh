#!/usr/bin/env bash
# Bump version across all files in kryptogo-meme-trader
# Usage: ./scripts/bump-version.sh <new_version>
# Example: ./scripts/bump-version.sh 2.6.0

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [ $# -ne 1 ]; then
  echo "Usage: $0 <new_version>"
  echo "Example: $0 2.6.0"
  exit 1
fi

NEW_VERSION="$1"

# Validate semver format
if ! echo "$NEW_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "Error: Version must be in semver format (e.g., 2.6.0)"
  exit 1
fi

# Files that contain the version
FILES=(
  "skill/package.json"
  "mcp-server/pyproject.toml"
  "skill/SKILL.md"
)

# Detect current version from package.json
CURRENT_VERSION=$(grep -oP '"version":\s*"\K[0-9]+\.[0-9]+\.[0-9]+' "$REPO_ROOT/skill/package.json")

if [ -z "$CURRENT_VERSION" ]; then
  echo "Error: Could not detect current version from skill/package.json"
  exit 1
fi

if [ "$CURRENT_VERSION" = "$NEW_VERSION" ]; then
  echo "Already at version $NEW_VERSION"
  exit 0
fi

echo "Bumping version: $CURRENT_VERSION → $NEW_VERSION"
echo ""

for file in "${FILES[@]}"; do
  filepath="$REPO_ROOT/$file"
  if [ -f "$filepath" ]; then
    sed -i "s/$CURRENT_VERSION/$NEW_VERSION/g" "$filepath"
    echo "  Updated: $file"
  else
    echo "  Skipped (not found): $file"
  fi
done

echo ""
echo "Done. Version bumped to $NEW_VERSION"
