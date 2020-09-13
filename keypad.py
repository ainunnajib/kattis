t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    a = []
    for __ in range(r):
        a.append(list(map(int, list(input()))))

    rows = [max(a[j]) for j in range(r)]
    cols = [max([a[j][i] for j in range(r)]) for i in range(c)]

    possible = True
    for j in range(r):
        for i in range(c):
            if a[j][i] == 0 and rows[j] == 1 and cols[i] == 1:
                possible = False
    if not possible:
        print('impossible')
    else:
        x = ''
        if sum(rows) == 1 or sum(cols) == 1:
            x = 'P'
        else:
            x = 'I'
        b = [['N' for i in range(c)] for j in range(r)]
        for j in range(r):
            for i in range(c):
                if a[j][i] == 1:
                    b[j][i] = x
        for r in b:
            print(''.join(r))

    print('----------')
