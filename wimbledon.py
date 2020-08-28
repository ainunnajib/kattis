players = []
umpires = []
n = int(input())
for _ in range(n):
    p, u = map(int, input().split())
    players.append(p)
    umpires.append(u)
count = 0
for k in range(n):
    for i in range(n):
        for j in range(i+1, n):
            if i != j and i!= k and j!= k:
                count += umpires[k]*players[i]*players[j]
print(count)
