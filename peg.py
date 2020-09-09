b = []
for _ in range(7):
    b.append(list(input()))
moves = 0
for i in range(7):
    for j in range(7):
        if i-2 >= 0 and i-2 < 7:
            if b[i-2][j] == '.' and b[i-1][j] == 'o' and b[i][j] == 'o':
                moves += 1
        if i+2 >= 0 and i+2 < 7:
            if b[i+2][j] == '.' and b[i+1][j] == 'o' and b[i][j] == 'o':
                moves += 1
        if j-2 >= 0 and j-2 < 7:
            if b[i][j-2] == '.' and b[i][j-1] == 'o' and b[i][j] == 'o':
                moves += 1
        if j+2 >= 0 and j+2 < 7:
            if b[i][j+2] == '.' and b[i][j+1] == 'o' and b[i][j] == 'o':
                moves += 1
print(moves)
