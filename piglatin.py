while True:
    try:
        s = input().split()
        a = []
        for w in s:
            if w[0] in 'aeiouy':
                a.append(w+'yay')
            else:
                i = 0
                while w[i] not in 'aeiouy':
                    i += 1
                a.append(w[i:]+w[:i]+'ay')
        r = a[0]
        for i in range(1,len(a)):
            r += ' '+a[i]
        print(r)
    except EOFError:
        break