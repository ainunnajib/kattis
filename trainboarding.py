n, l, p = map(int, input().split())
board = [0 for _ in range(n)]
maxwalk = 0
for _ in range(p):
    x = int(input())
    c = x//l
    c = min(c, n-1)
    board[c] += 1
    maxwalk = max(maxwalk, abs(x - c*l - l//2))
print(maxwalk)
print(max(board))