p = int(input())
for _ in range(p):
    case, x, y = map(int, input().split())
    if y == 0:
        print(case, 1, x)
    elif y > x:
        print(case, 2, x, y)
    else:
        b = y - x - 3
        down = 2 - b
        right = 2 + x
        up = y - b

        if 3 < down and down < right and right < up:
            print(case, 6, 1, 2, 3, down, right, up)
        else:
            print(case, 'NO PATH')
