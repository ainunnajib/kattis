r, c = map(int, input().split())
while r + c > 0:
    a = []
    b = []
    for j in range(r):
        a.append(list(input()))
    for i in range(c):
        s = ''
        for j in range(r):
            s += a[j][i]
        b.append(s)

    b.sort(key=str.casefold)

    for i in range(r):
        s = ''
        for j in range(c):
            s += b[j][i]
        print(s)

    r, c = map(int, input().split())
    if r + c > 0:
        print()
