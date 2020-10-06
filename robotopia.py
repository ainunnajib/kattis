n = int(input())
for _ in range(n):
    a, b, c, d, e, f = map(int, input().split())
    valid = []
    x = 1
    while a*x < e:
        if (e - a*x) % c == 0:
            y = (e - a*x) // c
            if y > 0 and b*x + d*y == f:
                valid.append((x, y))
        x += 1

    if len(valid) != 1:
        print('?')
    else:
        print(valid[0][0], valid[0][1])
