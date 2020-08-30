import sys

for line in sys.stdin.readlines():
    x, y, n, r = map(float, line.split())
    if x == 0 and y == 0 and n == 0 and r == 0:
        break
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
