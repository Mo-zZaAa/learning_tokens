#!/bin/bash
# usage: new_company.sh <name> <domain> <seed> : map only
export PLAYWRIGHT_BROWSERS_PATH=/root/.pwb
S=.claude/skills/company-site-wiki/scripts/sitewiki.py
python3 $S map --work KDX_사이트전수조사_인수인계/work/$1 --domain $2 --seed $3 2>&1 | tail -5
echo "MAPDONE $(date +%T)"
