from collections import defaultdict
r, c = map(int, input().split())
w = []
for _ in range(r):
    w.append(input())

columns = [[w[j][i] for j in range(r)] for i in range(c)]
printed = False
candel = 0
for j in range(r-1):
    d = defaultdict(int)
    for i in range(c):
        d[''.join(columns[i][j+1:])] += 1
    if max(d.values()) > 1:
        break
    else:
        candel += 1
print(candel)
