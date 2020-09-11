from collections import defaultdict
input()
n = int(input())
a = []
l = 0
for _ in range(n):
    s = input().split(', ')
    l = len(s)
    a.append(s)

d = defaultdict(list)
for i in range(n):
    inc = 0
    for j in range(n):
        inc = max(sum([a[i][x] != a[j][x] for x in range(l)]), inc)
    d[inc].append(a[i])

for x in d[min(d)]:
    print(', '.join(x))
