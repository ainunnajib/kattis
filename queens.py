n = int(input())
b = [[False for i in range(n)] for j in range(n)]
for _ in range(n):
    x, y = map(int, input().split())
    b[y][x] = True
valid = True
if sum([sum(r) for r in b]) != n:
    valid = False
for j in range(n):
    for i in range(n):
        if b[j][i]:
            if sum(b[j]) > 1:
                valid = False
            if sum(b[x][i] for x in range(n)) > 1:
                valid = False
            total = 0
            for d in range(1, n):
                if x+d >= 0 and x+d < n and y+d >= 0 and y+d < n:
                    if b[y+d][x+d]:
                        valid = False
                if x-d >= 0 and x-d < n and y-d >= 0 and y-d < n:
                    if b[y-d][x-d]:
                        valid = False
                if x+d >= 0 and x+d < n and y-d >= 0 and y-d < n:
                    if b[y-d][x+d]:
                        valid = False
                if x-d >= 0 and x-d < n and y+d >= 0 and y+d < n:
                    if b[y+d][x-d]:
                        valid = False

if valid:
    print('CORRECT')
else:
    print('INCORRECT')
