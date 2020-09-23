from collections import defaultdict
d = defaultdict(list)
n = int(input())
for _ in range(n):
    c, y = input().split()
    y = int(y)
    d[c].append(y)

for k in d:
    d[k].sort()

q = int(input())
for _ in range(q):
    c, t = input().split()
    t = int(t) - 1
    print(d[c][t])
