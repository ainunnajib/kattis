def dfs(g, v, node):
    v[node] = True
    for j in g[node]:
        if j not in v:
            dfs(g, v, j)

t = int(input())
for _ in range(t):
    n, m, l = map(int, input().split())

    g = [[] for i in range(n)]

    for __ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        g[a].append(b)

    visited = {}
    for __ in range(l):
        x = int(input()) - 1
        if x not in visited:
            dfs(g, visited, x)

    print(len(visited))
