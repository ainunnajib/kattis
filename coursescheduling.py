from collections import defaultdict
n = int(input())
d = defaultdict(set)
for _ in range(n):
    f, l, c = input().split()
    d[c].add(f+' '+l)
for k in sorted(d.keys()):
    print(k, len(d[k]))