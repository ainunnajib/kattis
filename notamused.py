from collections import defaultdict
day = 0
while True:
    try:
        s = input()
        if s == 'OPEN':
            if day > 0:
                print()
            day += 1
            d = defaultdict(int)
            e = defaultdict(int)
        elif s == 'CLOSE':
            print('Day', day)
            for x in sorted(d.keys()):
                print(x + ' $' + '{:.2f}'.format(d[x]/10))
        else:
            c, n, t = s.split()
            t = int(t)
            if c == 'ENTER':
                e[n] = t
            else:
                d[n] += t - e[n]
    except EOFError:
        break
