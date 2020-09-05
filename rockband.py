from collections import defaultdict

m, s = map(int, input().split())
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

d = defaultdict(int)
for i in range(s):
    for j in range(m):
        d[a[j][i]] += 1
    if len(d) == i+1:
        break

print(len(d))
l = []
for k in d:
    l.append(k)
l.sort()
l = map(str, l)
print(' '.join(l))
