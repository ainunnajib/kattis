b = []
for i in range(5):
    r = list(input())
    b.append([x == 'k' for x in r])
if sum([sum(r) for r in b]) != 9:
    print('invalid')
else:
    valid = True
    for j in range(5):
        for i in range(5):
            if b[j][i]:
                x, y = i+1, j+2
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i+1, j-2
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i-1, j+2
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i-1, j-2
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i+2, j+1
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i+2, j-1
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i-2, j+1
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
                x, y = i-2, j-1
                if x >= 0 and x < 5 and y >= 0 and y < 5:
                    if b[y][x]:
                        valid = False
    if valid:
        print('valid')
    else:
        print('invalid')
