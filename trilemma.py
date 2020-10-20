n = int(input())
for case in range(1, n+1):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    ss = []
    ss.append((x1-x2)**2 + (y1-y2)**2)
    ss.append((x1-x3)**2 + (y1-y3)**2)
    ss.append((x3-x2)**2 + (y3-y2)**2)
    ss.sort()

    aa, bb, cc = ss
    ans = ''
    if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1) or (x1-x2)*(y3-y2) == (x3-x2)*(y1-y2):
        ans = 'not a triangle'
    elif aa + bb == cc:
        if aa == bb:
            ans = 'isosceles right triangle'
        else:
            ans = 'scalene right triangle'
    elif aa + bb < cc:
        if aa == bb:
            ans = 'isosceles obtuse triangle'
        else:
            ans = 'scalene obtuse triangle'
    else:
        if aa == bb or bb == cc:
            ans = 'isosceles acute triangle'
        else:
            ans = 'scalene acute triangle'

    print(f'Case #{case}:', ans)
