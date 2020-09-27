from collections import defaultdict
d = defaultdict(list)
n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    d[x[i]].append(i)

answer = n
for k in d:
    if len(d[k]) > 1:
        d[k].sort()
        for i in range(len(d[k]) - 1):
            answer = min(answer, d[k][i+1] - d[k][i])

print(answer)
