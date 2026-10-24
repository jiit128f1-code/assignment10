
# Refactoring Metrics

| Measure | Before | After |
|---|---:|---:|
| Total lines in bill.py | [actual baseline count] | [actual final count] |
| Lines in the longest function | [measure baseline] | [measure final] |
| Number of places where slab arithmetic appears | 4 | 1 |
| Number of magic numbers left | [count baseline] | [count final] |
| Tests passing | 20 | 20 |

## Measurement method

- Line counts: `wc -l bill.py`
- Longest function: inspect function boundaries in VS Code
- Slab arithmetic: inspect the original and refactored calculation
- Magic numbers: inspect remaining numeric literals
- Tests: `python3 -m pytest -q`
