import math
r, h, s = map(int, input().split())
while r + h + s > 0:
    full = 2 * math.pi * r
    arc = math.acos(r/h) / math.pi * full
    line = math.sqrt(h**2 - r**2)
    total = (full - arc + 2 * line) * (100 + s) / 100

    print('{:.2f}'.format(round(total, 2)))

    r, h, s = map(int, input().split())
