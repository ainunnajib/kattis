players = []
umpires = []
n = int(input())
for _ in range(n):
    p, u = map(int, input().split())
    players.append(p)
    umpires.append(u)

pairs = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i+1, n):
        m = players[i]*players[j]
        pairs[i][j] = m
sumpairs = [sum(pairs[i]) for i in range(n)]

count = 0
for k in range(n):
    for i in range(n):
        if i != k:
            count += umpires[k] * (sumpairs[i] - pairs[i][k])
print(count)
