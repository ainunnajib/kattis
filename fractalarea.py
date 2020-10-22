import math
t = int(input())
for _ in range(t):
    r, n = map(int, input().split())

    area = math.pi * r**2
    if n > 1:
        area *= 2
        x = r/4
        k = 4
        for __ in range(3, n+1):
            area += 3 * k * (math.pi * x**2)
            x /= 2
            k *= 3

    print(area)
