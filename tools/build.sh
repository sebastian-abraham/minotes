#!/usr/bin/env bash
# Refresh the Markdown sources from the working folder, then rebuild the site.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NOTES="$HOME/study/Web Programming"
PY="$HOME/.venvs/study/bin/python"

FILES=(
  "START_HERE.md"
  "KIT_M1_WWW_HTML.md"
  "KIT_M2_CSS_JS.md"
  "KIT_M3_PHP.md"
  "KIT_M4_PHP_MYSQL.md"
  "KIT_M5_JSON_LARAVEL.md"
  "question_bank.md"
  "WEB PROGRAMING MOD-1.md"
  "module2_fixed.md"
  "module3.md"
  "module4.md"
  "module5.md"
  "wp_study_tracker.md"
  "wp_revision.md"
  "wp_code_drills.md"
)

DEST="$REPO/sources/web-programming"
mkdir -p "$DEST"

if [[ -d "$NOTES" ]]; then
  for f in "${FILES[@]}"; do
    [[ -f "$NOTES/$f" ]] && cp "$NOTES/$f" "$DEST/$f"
  done
  echo "sources synced from $NOTES"
else
  echo "note: $NOTES not found, building from existing sources"
fi

"$PY" "$REPO/tools/build.py"

echo
echo "Next:  git -C \"$REPO\" add -A && git -C \"$REPO\" commit -m 'notes update' && git -C \"$REPO\" push"
