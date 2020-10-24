from sys import stdin
for line in stdin.readlines():
    a, b, c = map(int, line.split())
    d = []
    r = []
    while c > 0:
        if a in r:
            repeat = d[r.index(a):]
            lr = len(repeat)
            d.extend(repeat * (c//lr))
            c %= lr
            d.extend(repeat[:c])
            break
        else:
            r.append(a)
            a *= 10
            x = a//b
            a %= b
            d.append(x)
            c -= 1

    print('0.', end = '')
    for x in d:
        print(x, end = '')
    print()
