m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
c = "#."
i, j = 0, 0
for _ in range(u):
    row = ""
    for __ in range(l + n + r):
        row += c[(i+j)%2]
        j += 1
    print(row)
    i += 1
    j = 0

for _ in range(m):
    s = input()
    row = ""
    for __ in range(l):
        row += c[(i+j)%2]
        j += 1
    row += s
    j += len(s)
    for __ in range(r):
        row += c[(i+j)%2]
        j += 1
    print(row)
    i += 1
    j = 0

for _ in range(d):
    row = ""
    for __ in range(l + n + r):
        row += c[(i+j)%2]
        j += 1
    print(row)
    i += 1
    j = 0
