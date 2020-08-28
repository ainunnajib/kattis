players = []
umpires = []
n = int(input())
for _ in range(n):
    p, u = map(int, input().split())
    players.append(p)
    umpires.append(u)

sumplayers = sum(players)
sumumpires = sum(umpires)

sumtwins = 0
sumplayerumpiretwins = 0
sumtriplets = 0
for i in range(n):
    sumtwins += players[i]*players[i]
    sumplayerumpiretwins += players[i]*umpires[i]
    sumtriplets += players[i]*players[i]*umpires[i]

count = sumumpires*sumplayers*sumplayers
count -= sumumpires*sumtwins
count //= 2
count -= sumplayerumpiretwins*sumplayers
count += sumtriplets

print(count)
