import math
x, lo, hi = map(int, input().split())

k = 0
f = x
while math.ceil(f) < lo:
    f = 10 * math.sqrt(f)
    k += 1
if f > hi:
    print('impossible')
else:
    a = k
    if hi == 100:
        b = 'inf'
    else:
        while math.ceil(f) <= hi:
            f = 10 * math.sqrt(f)
            k += 1
        b = k - 1

    print(a, b)
