import math

lognfact = [0 for i in range(100001)]
for i in range(1, 100001):
    lognfact[i] = lognfact[i-1] + math.log(i)

n = int(input())
while n > 0:
    logsn = (math.log(2) + math.log(math.pi) + math.log(n))/2 + n * (math.log(n) - 1)

    print(math.exp(lognfact[n] - logsn))

    n = int(input())
