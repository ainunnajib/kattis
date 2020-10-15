import sys
sys.setrecursionlimit(10**5)

def nexts(rd, cd, s):
    if s == 'top':
        if rd == 1:
            return 'down'
        if rd == -1:
            return 'up'
        if cd == 1:
            return 'right'
        if cd == -1:
            return 'left'
    if s == 'bottom':
        if rd == 1:
            return 'up'
        if rd == -1:
            return 'down'
        if cd == 1:
            return 'left'
        if cd == -1:
            return 'right'
    if s == 'left':
        if rd == 1:
            return 'left'
        if rd == -1:
            return 'left'
        if cd == 1:
            return 'top'
        if cd == -1:
            return 'bottom'
    if s == 'right':
        if rd == 1:
            return 'right'
        if rd == -1:
            return 'right'
        if cd == 1:
            return 'bottom'
        if cd == -1:
            return 'top'
    if s == 'up':
        if rd == 1:
            return 'top'
        if rd == -1:
            return 'bottom'
        if cd == 1:
            return 'up'
        if cd == -1:
            return 'up'
    if s == 'down':
        if rd == 1:
            return 'bottom'
        if rd == -1:
            return 'top'
        if cd == 1:
            return 'down'
        if cd == -1:
            return 'down'

def dfs(n, g, v, t, rh, ch):
    if t in v:
        return False
    v.add(t)

    r, c, s = t
    if r == rh and c == ch and s == 'bottom':
        return True
    if g[r][c] == '*':
        return False

    possible = False

    if r - 1 >= 0:
        possible = possible or dfs(n, g, v, (r-1, c, nexts(-1, 0, s)), rh, ch)
    if r + 1 < n:
        possible = possible or dfs(n, g, v, (r+1, c, nexts(1, 0, s)), rh, ch)
    if c - 1 >= 0:
        possible = possible or dfs(n, g, v, (r, c-1, nexts(0, -1, s)), rh, ch)
    if c + 1 < n:
        possible = possible or dfs(n, g, v, (r, c+1, nexts(0, 1, s)), rh, ch)

    return possible

t = int(input())
for _ in range(t):
    n = int(input())
    g = []
    for r in range(n):
        row = list(input())
        g.append(row)
        if 'S' in row:
            rs, cs = r, row.index('S')
        if 'H' in row:
            rh, ch = r, row.index('H')

    v = set()
    possible = dfs(n, g, v, (rs, cs, 'left'), rh, ch)
    print('Yes' if possible else 'No')
