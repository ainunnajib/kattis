from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n):
    d[input()] += 1

mind = min(d.values())
l = []
for x in d:
    if d[x] == mind:
        l.append(x)
l.sort()
for x in l:
    print(x)
