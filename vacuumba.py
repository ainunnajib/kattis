import math
n = int(input())
for _ in range(n):
    m = int(input())
    x, y, t = 0.0, 0.0, 90.0
    for __ in range(m):
        a, d = map(float, input().split())
        t += a
        if t > 360:
            t -= 360
        if t < 0:
            t += 360
        x += math.cos(math.pi*(t/180)) * d
        y += math.sin(math.pi*(t/180)) * d
    print(x, y)
