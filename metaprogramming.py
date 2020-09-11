d = {}
while True:
    try:
        s = input().split()
        if s[0] == 'define':
            d[s[2]] = int(s[1])
        else:
            x = s[1]
            o = s[2]
            y = s[3]
            if x in d and y in d:
                if o == '=':
                    print('true' if d[x] == d[y] else 'false')
                elif o == '<':
                    print('true' if d[x] < d[y] else 'false')
                elif o == '>':
                    print('true' if d[x] > d[y] else 'false')
            else:
                print('undefined')
    except EOFError:
        break
