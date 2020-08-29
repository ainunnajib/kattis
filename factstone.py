import math
y = int(input())
while y > 0:
    y -= 1960
    y //= 10
    y += 2
    bits = 2**y
    n = 1
    while bits > 0:
        n += 1
        bits -= math.log(n, 2)
    print(n-1)
    y = int(input())
