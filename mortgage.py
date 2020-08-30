x, y, n, r = map(float, input().split())
while x != 0 or y != 0 or n != 0 or r != 0:
    r /= 100
    r /= 12
    n *= 12
    if r != 0:
        balance = x * ((r+1)**n) - y * (((r+1)**n)-1)/r
    else:
        balance = x - y*n
    if balance > 0:
        print('NO')
    else:
        print('YES')
    x, y, n, r = map(float, input().split())
