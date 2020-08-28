players = []
umpires = []
n = int(input())
for _ in range(n):
    p, u = map(int, input().split())
    players.append(p)
    umpires.append(u)

sumpairs = []
for i in range(n):
    sum = 0
    for j in range(n):
        if i != j:
            sum += players[i]*players[j]
    sumpairs.append(sum)

count = 0
for k in range(n):
    for i in range(n):
        if i != k:
            count += umpires[k] * (sumpairs[i] - players[i]*players[k])
print(count//2)
