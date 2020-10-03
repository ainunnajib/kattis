s = input()
while s != '0':
    l = []
    nf, nr = map(int, s.split())
    f = list(map(int, input().split()))
    r = list(map(int, input().split()))
    for x in f:
        for y in r:
            l.append(1.0*y/x)
    l.sort()
    maxspread = 1.0
    for i in range(len(l)-1):
        spread = l[i+1]/l[i]
        maxspread = max(maxspread, spread)
    print('%.2f' % round(maxspread, 2))

    s = input()
