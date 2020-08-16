l = input().split()
r = int(l[0])
c = int(l[1])
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
inline = True
count = 0
for line in cols:
    if line != ref:
        if (inline):
            count += 1
        inline = False
    else:
        inline = True
print(count)