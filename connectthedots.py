r = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
board = []
while True:
    try:
        while True:
            board = []
            s = input()
            while s!= "":
                board.append([c for c in s])
                s = input()
            for i in range(61):
                c = r[i]
                d = r[i+1]
                a, b, x, y = -1, -1, -1, -1
                for j in range(len(board)):
                    if c in board[j]:
                        b = j
                        a = board[j].index(c)
                        break
                if a < 0:
                    break
                for j in range(len(board)):
                    if d in board[j]:
                        y = j
                        x = board[j].index(d)
                        break
                # draw line from (a,b) to (x,y)
                if a == x: #vertical line
                    p = min(b,y)
                    q = max(b,y)
                    for j in range(1,q-p):
                        if board[p+j][x] == '.':
                            board[p+j][x] = '|'
                        elif board[p+j][x] == '-':
                            board[p+j][x] = '+'
                elif b == y: #horizontal line
                    p = min(a,x)
                    q = max(a,x)
                    for j in range(1,q-p):
                        if board[y][p+j] == '.':
                            board[y][p+j] = '-'
                        elif board[y][p+j] == '|':
                            board[y][p+j] = '+'
            for row in board:
                print(''.join(row))
            print()
    except EOFError:
        for i in range(61):
            c = r[i]
            d = r[i+1]
            a, b, x, y = -1, -1, -1, -1
            for j in range(len(board)):
                if c in board[j]:
                    b = j
                    a = board[j].index(c)
                    break
            if a < 0:
                break
            for j in range(len(board)):
                if d in board[j]:
                    y = j
                    x = board[j].index(d)
                    break
            # draw line from (a,b) to (x,y)
            if a == x: #vertical line
                p = min(b,y)
                q = max(b,y)
                for j in range(1,q-p):
                    if board[p+j][x] == '.':
                        board[p+j][x] = '|'
                    elif board[p+j][x] == '-':
                        board[p+j][x] = '+'
            elif b == y: #horizontal line
                p = min(a,x)
                q = max(a,x)
                for j in range(1,q-p):
                    if board[y][p+j] == '.':
                        board[y][p+j] = '-'
                    elif board[y][p+j] == '|':
                        board[y][p+j] = '+'
        for row in board:
            print(''.join(row))
        print()
        break
