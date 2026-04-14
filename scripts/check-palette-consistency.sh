#!/usr/bin/env bash
# Validate that every hex color in port theme files exists in palette.json.
# Skips .lua files (neovim theme IS the palette source) and README files.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PALETTE="$REPO_ROOT/palette.json"

if [[ ! -f "$PALETTE" ]]; then
  echo "ERROR: palette.json not found at $PALETTE"
  exit 1
fi

# Build lookup set of all valid hex colors (lowercase) from both dark and light palettes
valid_colors=$(jq -r '(.dark // {}), (.light // {}) | to_entries[] | .value' "$PALETTE" | tr '[:upper:]' '[:lower:]' | sort -u)

exit_code=0

# Scan port files for hex color literals
while IFS= read -r file; do
  # Skip Lua files (neovim theme defines the palette — checking is circular)
  [[ "$file" == *.lua ]] && continue
  # Skip READMEs and palette.json itself
  [[ "$(basename "$file")" == README.md ]] && continue
  [[ "$file" == "$PALETTE" ]] && continue

  line_num=0
  while IFS= read -r line; do
    line_num=$((line_num + 1))

    # Extract all #RRGGBB patterns from the line
    colors=$(echo "$line" | grep -oiE '#[0-9a-fA-F]{6}' || true)
    for color in $colors; do
      color_lower=$(echo "$color" | tr '[:upper:]' '[:lower:]')
      if ! echo "$valid_colors" | grep -qx "$color_lower"; then
        rel_path="${file#"$REPO_ROOT"/}"
        echo "MISMATCH: $rel_path:$line_num — $color is not in palette.json"
        exit_code=1
      fi
    done
  done < "$file"
done < <(find "$REPO_ROOT/ports" -type f ! -name '*.md')

if [[ $exit_code -eq 0 ]]; then
  echo "All colors match palette.json"
fi

exit $exit_code
