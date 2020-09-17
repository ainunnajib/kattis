b = []
for _ in range(4):
    b.append(list(map(int, input().split())))
m = int(input())

for _ in range(m):
    c = [[b[i][j] for i in range(4)] for j in range(3,-1,-1)]
    b = c

result = []
for row in b:
    r = []
    o = []
    for c in row:
        if c == 0:
            o.append(c)
        else:
            r.append(c)
    r.extend(o)
    i = 1
    while i < 4 and r[i] > 0:
        if r[i-1] == r[i]:
            r[i-1] *= 2
            r.pop(i)
            r.append(0)
        i += 1
    result.append(r)

for _ in range(m):
    c = [[result[i][j] for i in range(3,-1,-1)] for j in range(4)]
    result = c

for row in result:
    print(' '.join(list(map(str, row))))
