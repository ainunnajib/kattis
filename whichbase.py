p = int(input())
for _ in range(p):
    k, v = input().split()

    o = 0
    x = 1
    for c in v[::-1]:
        d = int(c)
        if d > 7:
            o = 0
            break
        o += d * x
        x *= 8

    h = 0
    x = 1
    for c in v[::-1]:
        d = int(c)
        h += d * x
        x *= 16

    print(k, o, int(v), h)
