m, s = map(int, input().split())
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))
d = {}
for j in range(m):
    d[a[j][0]] = True

while len(d) < s:
    l = []
    for k in d:
        for j in range(m):
            for i in range(a[j].index(k)+1):
                if a[j][i] not in d:
                    l.append(a[j][i])
    if l == []:
        break
    else:
        for x in l:
            d[x] = True
print(len(d))
l = []
for k in d:
    l.append(k)
l.sort()
l = map(str, l)
print(' '.join(l))
