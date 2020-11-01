n, m = map(int, input().split())
s = [[True for j in range(n)] for i in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    s[r][c] = False

minmoves = n*n
for p in range(1, m+1):
    if m%p == 0:
        q = m//p
        for i in range(n+1-p):
            for j in range(n+1-q):
                moves = sum([sum(s[x][j:j+q]) for x in range(i, i+p)])
                minmoves = min(minmoves, moves)
print(minmoves)
