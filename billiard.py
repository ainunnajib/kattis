import math
a, b, s, m, n = map(int, input().split())
while a + b + s + m + n > 0:
    h = m * a
    v = n * b

    angle = round(180 * math.atan2(v, h) / math.pi, 2)
    speed = round(math.sqrt(h**2 + v**2) / s, 2)

    print('{:.2f}'.format(angle), '{:.2f}'.format(speed))

    a, b, s, m, n = map(int, input().split())
