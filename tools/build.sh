#!/usr/bin/env bash
# Refresh the Markdown sources from the working folders, then rebuild the site.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$HOME/.venvs/study/bin/python"

sync_dir() {  # sync_dir "<source folder>" "<repo subject folder>"
  local src="$1" dest="$REPO/sources/$2"
  mkdir -p "$dest"
  if [[ -d "$src" ]]; then
    find "$src" -maxdepth 1 -name '*.md' -print0 | while IFS= read -r -d '' f; do
      cp "$f" "$dest/"
    done
    echo "sources synced: $src -> sources/$2"
  else
    echo "note: $src not found, building from committed sources"
  fi
}

sync_dir "$HOME/study/Web Programming" "web-programming"
sync_dir "$HOME/study/EHS" "ehs"
sync_dir "$HOME/study/ISE" "ise"

# Compiler Lab: the docs and programs live in the lab repo, not under ~/study.
LAB="$HOME/projects/mainproject"
if [[ -d "$LAB" ]]; then
  cp "$LAB/ALGORITHMS.md" "$LAB/EXAM_DRILLS.md" "$REPO/sources/compiler-lab/" 2>/dev/null || true
  cp "$LAB"/study/GROUP_*.md "$REPO/sources/compiler-lab/" 2>/dev/null || true
  for f in lex_a.c lexer.l lex_count.l lex_id.l yacc_id.y e_closure.c e-nfa_nfa.c \
           nfa_dfa.c fnf.c rdp.c srp.c intermediate.c input.c; do
    [[ -f "$LAB/$f" ]] && cp "$LAB/$f" "$REPO/sources/compiler-lab/code/"
  done
  echo "sources synced: $LAB -> sources/compiler-lab"
else
  echo "note: $LAB not found, building compiler-lab from committed sources"
fi

"$PY" "$REPO/tools/build.py"

echo
echo "Next:  git -C \"$REPO\" add -A && git -C \"$REPO\" commit -m 'notes update' && git -C \"$REPO\" push"
