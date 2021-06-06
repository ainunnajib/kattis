from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(int)
for _ in range(n):
    for i in set(input().split()):
        d[i] += 1
l = []
for k in d:
    if d[k] == n:
        l.append(k)
l.sort()
print(len(l))
for x in l:
    print(x)