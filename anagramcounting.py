from sys import stdin
from collections import defaultdict

f = [1 for _ in range(101)]
for i in range(2, 101):
    f[i] = f[i-1] * i

for line in stdin.readlines():
    w = line.strip()
    d = defaultdict(int)
    for c in w:
        d[c] += 1

    ans = f[len(w)]
    for k in d:
        ans //= f[d[k]]

    print(ans)
