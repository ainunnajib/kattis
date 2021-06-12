from sys import *
line = stdin.readline()
while line != '':
    s = list(map(int, line.split()))
    n = s[0]
    m = s[1]
    moves = set(s[2:])
    iwin = [False for _ in range(n+1)]
    for i in range(1, n+1):
        for move in moves:
            if i >= move and not iwin[i-move]:
                iwin[i] = True
                break

    if iwin[n]:
        print('Stan wins')
    else:
        print('Ollie wins')

    line = stdin.readline()
