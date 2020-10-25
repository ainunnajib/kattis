t = int(input())
for _ in range(t):
    r, c = map(int, input().split())

    bottom, right = 0, 0
    level = 0
    while r > bottom or c > right:
        level += 1
        if level % 2 == 1:
            right = 2**((level+1)//2) - 1
        else:
            bottom = 2**(level//2) - 1

    rows = bottom + 1
    cols = right + 1
    num = rows*cols//2
    if level % 2 == 1:
        c -= cols//2
        num += rows * c + r
    else:
        r -= rows//2
        num += cols * r + c

    print(num)
