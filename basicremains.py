s = input().split()
while s[0] != '0':
    b = int(s[0])

    p = 0
    x = 1
    for c in s[1][::-1]:
        p += int(c) * x
        x *= b

    m = 0
    x = 1
    for c in s[2][::-1]:
        m += int(c) * x
        x *= b

    v = p % m
    if v == 0:
        a = ['0']
    else:
        a = []
        while v > 0:
            a.append(str(v%b))
            v //= b

    print(''.join(a[::-1]))

    s = input().split()
