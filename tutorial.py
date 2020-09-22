import math
m, n, t = map(int, input().split())
x = n
accepted = True
if t == 1:
    while n > 1 and x <= m:
        n -= 1
        x *= n
elif t == 2:
    x = 2
    while n > 1 and x <= m:
        n -= 1
        x *= 2
elif t in [3, 4, 5]:
    t = 7 - t
    x = 1
    while t > 0 and x <= m:
        x *= n
        t -= 1
elif t == 6:
    x *= math.log2(n)
elif t == 7:
    pass

if x > m:
    accepted = False
if accepted:
    print('AC')
else:
    print('TLE')
