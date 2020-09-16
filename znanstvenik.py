from collections import defaultdict
r, c = map(int, input().split())
w = []
for _ in range(r):
    w.append(input())

columns = [''.join([w[j][i] for j in range(r)]) for i in range(c)]

candel = 0
for j in range(r-1):
    d = defaultdict(int)
    maxv = 0
    for i in range(c):
        s = columns[i][j+1:]
        d[s] += 1
        maxv = max(maxv, d[s])
        if maxv > 1:
            break
    if maxv > 1:
        break
    else:
        candel += 1
print(candel)
