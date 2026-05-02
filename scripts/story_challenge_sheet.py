#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone

TEMPLATE = """# Story challenge sheet

- Generated: {ts}
- Candidate: {candidate}

## 1) Testable question

## 2) Three required evidence checks
1. 
2. 
3. 

## 3) Falsifier

## 4) Baseline comparator(s)

## 5) Independent corroboration family

## 6) Non-specialist decision consequence

## 7) Disconfirming query run
- Query:
- Result:

## 8) Disposition
- publish / rotate / hold
- reason:
"""

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidate', default='')
    ap.add_argument('--out', required=True)
    a=ap.parse_args()
    ts=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(a.out,'w') as f:
        f.write(TEMPLATE.format(ts=ts,candidate=a.candidate))
    print(a.out)
