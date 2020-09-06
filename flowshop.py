n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
end = [[0 for i in range(m)] for j in range(n)]
for j in range(n):
    for i in range(m):
        if j == 0:
            if i == 0:
                end[j][i] = a[j][i]
            else:
                end[j][i] = end[j][i-1] + a[j][i]
        else:
            if i == 0:
                end[j][i] = end[j-1][i] + a[j][i]
            else:
                end[j][i] = max(end[j][i-1], end[j-1][i]) + a[j][i]
r = []
for j in range(n):
    r.append(str(end[j][-1]))
print(' '.join(r))
