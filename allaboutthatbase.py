digits = '0123456789abcdefghijklmnopqrstuvwxyz'
minbase = {}
v = {}
for i in range(36):
    v[digits[i]] = i
    minbase[digits[i]] = i + 1

t = int(input())
for _ in range(t):
    x, o, y, __, r = input().split()
    if o == '/':
        if y == '0' * len(y):
            print('invalid')
            continue

        o = '*'
        x, r = r, x
    if o == '-':
        o = '+'
        x, r = r, x

    if '1' * len(x) == x and '1' * len(y) == y and '1' * len(r) == r:
        startbase = 1
    else:
        startbase = 2
        for c in x:
            startbase = max(startbase, minbase[c])
        for c in y:
            startbase = max(startbase, minbase[c])
        for c in r:
            startbase = max(startbase, minbase[c])

    sym = '_123456789abcdefghijklmnopqrstuvwxyz0'
    valid = []
    for b in range(startbase, 37):
        xval = 0
        mul = 1
        for c in x[::-1]:
            xval += v[c] * mul
            mul *= b

        yval = 0
        mul = 1
        for c in y[::-1]:
            yval += v[c] * mul
            mul *= b

        rval = 0
        mul = 1
        for c in r[::-1]:
            rval += v[c] * mul
            mul *= b

        if (o == '+' and xval + yval == rval) or (o == '*' and xval * yval == rval):
            valid.append(sym[b])

    if len(valid) == 0:
        print('invalid')
    else:
        print(''.join(valid))
