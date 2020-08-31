n = int(input())
a = list(map(int, input().split()))

maxa = []
maxp = -1
for x in a:
    maxa.append(maxp)
    if x > maxp:
        maxp = x

mina = [-1 for i in range(n)]
minp = a[-1]
for i in range(n-1,-1,-1):
    mina[i] = minp
    if a[i] < minp:
        minp = a[i]
mina[-1] = -1

c = 0
for i in range(n):
    c += int( (maxa[i] <= a[i] or maxa[i] == -1) and (mina[i] >= a[i] or mina[i] == -1) )

print(c)
