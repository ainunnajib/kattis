d = {}
s = input()
while s != '':
    s = s.split()
    d[s[1]] = s[0]
    s = input()
while True:
    try:
        s = input()
        if s in d.keys():
            print(d[s])
        else:
            print('eh')
    except EOFError:
        break