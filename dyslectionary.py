first = True
while True:
    try:
        if not first:
            print()
        first = False
        l = []
        maxlen = 0
        s = input()
        while s != '':
            maxlen = max(maxlen, len(s))
            l.append(s[::-1])
            s = input()
        l.sort()
        for x in l:
            print(' ' * (maxlen - len(x)) + x[::-1])
    except EOFError:
        l.sort()
        for x in l:
            print(' ' * (maxlen - len(x)) + x[::-1])
        break
