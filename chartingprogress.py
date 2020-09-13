while True:
    try:
        a = []
        s = input()
        while s != '':
            a.append(list(s))
            s = input()
        r = len(a)
        c = len(a[0])
        cols = [[a[j][i] for j in range(r)] for i in range(c)]
        columns = [(cols[i].index('*'), cols[i]) for i in range(c)]
        columns.sort(reverse = True)
        rows = [[columns[i][1][j] for i in range(c)] for j in range(r)]
        for r in rows:
            print(''.join(r))
        print()
    except EOFError:
        r = len(a)
        c = len(a[0])
        cols = [[a[j][i] for j in range(r)] for i in range(c)]
        columns = [(cols[i].index('*'), cols[i]) for i in range(c)]
        columns.sort(reverse = True)
        rows = [[columns[i][1][j] for i in range(c)] for j in range(r)]
        for r in rows:
            print(''.join(r))
        break
