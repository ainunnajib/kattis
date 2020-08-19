board = []
r = {(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1),(0,1):(1,0)}
l = {(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}
row = 7
col = 0
facing = (0,1)
for _ in range(8):
    s = input()
    board.append([c for c in s])
board[7][0] = '.'
bug = False
s = input()
for c in s:
    if c == 'F':
        row += facing[0]
        col += facing[1]
        if row < 0 or col < 0 or row > 7 or col > 7:
            bug = True
            break
        if board[row][col] in ['C','I']:
            bug = True
            break
    elif c == 'R':
        facing = r[facing]
    elif c == 'L':
        facing = l[facing]
    elif c == 'X':
        if board[row + facing[0]][col + facing[1]] == 'I':
            board[row + facing[0]][col + facing[1]] = '.'
        else:
            bug = True
            break
if bug:
    print("Bug!")
elif board[row][col] == 'D':
    print("Diamond!")
else:
    print("Bug!")
