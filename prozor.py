r, s, k = map(int, input().split())
b = []
for _ in range(r):
    b.append(list(input()))

ansi, ansj = 0, 0
maxhit = 0
for i in range(r-k+1):
    for j in range(s-k+1):
        hit = sum([b[x][j+1:j+k-1].count('*') for x in range(i+1, i+k-1)])
        if hit > maxhit:
            maxhit = hit
            ansi = i
            ansj = j
print(maxhit)
b[ansi][ansj] = '+'
b[ansi][ansj+k-1] = '+'
b[ansi+k-1][ansj] = '+'
b[ansi+k-1][ansj+k-1] = '+'
for i in range(ansi+1, ansi+k-1):
    b[i][ansj] = '|'
    b[i][ansj+k-1] = '|'
for j in range(ansj+1, ansj+k-1):
    b[ansi][j] = '-'
    b[ansi+k-1][j] = '-'
for r in b:
    print(''.join(r))
