r, c = map(int, input().split())
d = []
for i in range(r):
    d.append(input())
cols = []
for i in range(c):
    s = ""
    for j in range(r):
        s += d[j][i]
    cols.append(s)
ref = '_' * r
print(cols.count(ref)+1)
