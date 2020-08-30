import sys
from collections import defaultdict

inputs = iter(sys.stdin.readlines())
n, m = map(int, next(inputs).split())
while n + m > 0:
    d = defaultdict(int)
    for _ in range(n+m):
        d[int(next(inputs))] += 1
    count = 0
    for v in d.values():
        if v == 2:
            count += 1
    print(count)
    n, m = map(int, next(inputs).split())
