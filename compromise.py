t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    b = []
    for __ in range(n):
        b.append(list(map(int, list(input()))))
    r = ''
    for i in range(m):
        s = 0
        for j in range(n):
            s += b[j][i]
        if 2*s >= n:
            r += '1'
        else:
            r += '0'
    print(r)
