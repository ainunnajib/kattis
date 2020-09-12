n, k = map(int, input().split())
a = []
d = []
h = []
for i in range(n):
    x, y, z = map(int, input().split())
    a.append((x, i))
    d.append((y, i))
    h.append((z, i))
s = {}
a.sort(reverse = True)
d.sort(reverse = True)
h.sort(reverse = True)
for x in a[:k]:
    s[x[1]] = True
for y in d[:k]:
    s[y[1]] = True
for z in h[:k]:
    s[z[1]] = True
print(len(s))
