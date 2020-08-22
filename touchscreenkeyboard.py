def dist(w1, w2):
    board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    distance = 0
    w1r, w1c, w2r, w2c = 0, 0, 0, 0
    for i in range(len(w1)):
        x = w1[i]
        y = w2[i]
        for row in range(3):
            if x in board[row]:
                w1r = row
                w1c = board[row].index(x)
            if y in board[row]:
                w2r = row
                w2c = board[row].index(y)
        distance += abs(w1r-w2r) + abs(w1c-w2c)
    return distance

t = int(input())
for _ in range(t):

    a = input().split()
    word = a[0]
    n = int(a[1])

    d = {}
    l = []
    for __ in range(n):
        w = input()
        di = dist(word, w)
        if di not in l:
            l.append(di)
            d[di] = [w]
        else:
            d[di].append(w)
    l.sort()
    for x in l:
        for y in sorted(d[x]):
            print(y, x)
