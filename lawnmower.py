nx, ny, w = input().split()
while nx != '0' and ny != '0':
    nx = int(nx)
    ny = int(ny)
    w = float(w)
    h = w/2
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    a = [(i-h, i+h) for i in x]
    a.sort()
    b = [(j-h, j+h) for j in y]
    b.sort()
    gapx = False
    prevx = 0
    for t in a:
        if t[0] > prevx:
            gapx = True
            break
        prevx = t[1]
    if a[-1][1] < 75:
        gapx = True

    gapy = False
    prevy = 0
    for t in b:
        if t[0] > prevy:
            gapy = True
            break
        prevy = t[1]
    if b[-1][1] < 100:
        gapy = True

    if gapx or gapy:
        print('NO')
    else:
        print('YES')

    nx, ny, w = input().split()
