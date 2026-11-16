#!/bin/bash
# usage: fetch_loop.sh <workdir> [extra fetch args...]  : fetch until 대기 0, then digest
export PLAYWRIGHT_BROWSERS_PATH=/root/.pwb
S=.claude/skills/company-site-wiki/scripts/sitewiki.py
W=$1; shift
for i in $(seq 1 40); do
  out=$(python3 $S fetch --work "$W" --minutes 8 "$@" 2>&1 | tail -1); echo "$(date +%T) $out"
  echo "$out" | grep -q "'대기'" || break
done
python3 $S digest --work "$W" 2>&1 | tail -2
echo "DONE $(date +%T)"
