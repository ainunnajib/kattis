import sys
from collections import defaultdict

inputs = iter(sys.stdin.readlines())
n, m = map(int, next(inputs).split())
while n + m > 0:
    d = set()
    for _ in range(n):
        d.add(int(next(inputs)))
    for _ in range(m):
        d.discard(int(next(inputs)))
    print(n-len(d))
    n, m = map(int, next(inputs).split())
