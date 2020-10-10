from sys import stdin, stdout
from collections import defaultdict

d = defaultdict(int)
total = 0
for line in stdin.readlines():
    d[line.strip()] += 1
    total += 1

for k in sorted(d.keys()):
    print(k, 100.0 * d[k] / total)
