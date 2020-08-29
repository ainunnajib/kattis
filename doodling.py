n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    d = {}
    x = 0
    y = 0
    dir = [1, 1]
    if x + dir[0] >= 0 and x + dir[0] < a and y + dir[1] >= 0 and y + dir[1] < b:
        d[(x, y)] = 1
        x += dir[0]
        y += dir[1]
    while (x not in [0, a-1] or y not in [0, b-1]):
        if (x, y) not in d:
            d[(x, y)] = 1
        if x + dir[0] >= 0 and x + dir[0] < a and y + dir[1] >= 0 and y + dir[1] < b:
            x += dir[0]
            y += dir[1]
        else:
            if x in [0, a-1]: # hit vertical
                dir[0] *= -1
            elif y in [0, b-1]: # hit horizontal
                dir[1] *= -1
            x += dir[0]
            y += dir[1]
    print(len(d)+1)
