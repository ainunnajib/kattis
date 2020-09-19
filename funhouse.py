d = {'/':{(1, 0):(0, -1), (-1, 0):(0, 1), (0, 1):(-1, 0), (0, -1):(1, 0)},
    '\\':{(1, 0):(0, 1), (-1, 0):(0, -1), (0, 1):(1, 0), (0, -1):(-1, 0)}}

w, l = map(int, input().split())
house = 0
while w + l > 0:
    house += 1
    b = []
    e = (0, 0)
    for i in range(l):
        s = list(input())
        b.append(s)
        if '*' in s:
            e = (i, s.index('*'))

    dir = (0, 0)
    if e[0] == 0:
        dir = (1, 0)
    elif e[0] == l-1:
        dir = (-1, 0)
    elif e[1] == 0:
        dir = (0, 1)
    else:
        dir = (0, -1)

    i, j = e
    x = b[i][j]
    while x != 'x':
        if x in '/\\':
            dir = d[x][dir]
        i += dir[0]
        j += dir[1]
        x = b[i][j]
    b[i][j] = '&'

    print('HOUSE', house)
    for r in b:
        print(''.join(r))

    w, l = map(int, input().split())
