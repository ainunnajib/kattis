d = {}
s = input()
while s != '0':
    if '=' in s:
        s = s.split(' = ')
        d[s[0]] = int(s[1])
    else:
        s = s.split(' + ')
        n = 0
        l = []
        for x in s:
            if x.isdigit():
                n += int(x)
            elif x in d:
                n += d[x]
            else:
                l.append(x)
        if len(l) == 0:
            print(n)
        else:
            r = ''
            if n > 0:
                r = str(n)
            for x in l:
                if len(r) == 0:
                    r = x
                else:
                    r += ' + ' + x
            print(r)
    s = input()
