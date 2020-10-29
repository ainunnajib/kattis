s, x, y, dx, dy = map(int, input().split())
while s + x + y + dx + dy > 0:
    ss = 2*s
    impossible = False
    d = set()
    jump = 0
    while (x//s + y//s) % 2 == 0 or x%s == 0 or y%s == 0:
        if (x%ss, y%ss) in d:
            impossible = True
            break
        else:
            d.add((x%ss, y%ss))

        jump += 1
        x += dx
        y += dy

    if impossible:
        print('The flea cannot escape from black squares.')
    else:
        print(f'After {jump} jumps the flea lands at ({x}, {y}).')

    s, x, y, dx, dy = map(int, input().split())
