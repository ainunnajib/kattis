lostto = {'R':'P', 'P':'S', 'S':'R'}
t = int(input())
for _ in range(t):
    r, c, n = map(int, input().split())
    board = []
    for __ in range(r):
        board.append([x for x in input()])
    for __ in range(n):
        nextboard = []
        for i in range(r):
            nextboard.append([])
            for j in range(c):
                x = board[i][j]
                xkiller = lostto[x]
                adj = ""
                if i > 0:
                    adj += board[i-1][j]
                if j > 0:
                    adj += board[i][j-1]
                if i+1 < r:
                    adj += board[i+1][j]
                if j+1 < c:
                    adj += board[i][j+1]
                if xkiller in adj:
                    nextboard[i].append(xkiller)
                else:
                    nextboard[i].append(x)
        board = nextboard
    for i in range(r):
        print(''.join(board[i]))
    if _ < t-1:
        print()
