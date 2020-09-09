def dfs(g, v, node):
    v[node] = True
    for j in range(len(g[node])):
        if g[node][j] and j not in v:
            dfs(g, v, j)

n = int(input())
for _ in range(n):
    m = int(input())
    g = [[False for i in range(m)] for j in range(m)]
    r = int(input())
    for __ in range(r):
        a, b = map(int, input().split())
        g[a][b] = True
        g[b][a] = True
    cc = 0
    visited = {}
    for x in range(m):
        if x not in visited:
            cc += 1
            dfs(g, visited, x)
    print(cc-1)
