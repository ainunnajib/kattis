d = {}
while True:
    try:
        s = input().split()
        for i in range(len(s)):
            if s[i].lower() in d:
                s[i] = '.'
            else:
                d[s[i].lower()] = True
        print(' '.join(s))
    except EOFError:
        break
