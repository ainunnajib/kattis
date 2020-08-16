import math
p, a, b, c, d, n = map(int, input().split())
largestprior = 0
smallestsofar = 0
gap = 0
for k in range(1, n+1):
    price = p*(math.sin(a*k+b) + math.cos(c*k+d) + 2)
    gap = max(gap, largestprior - price)
    largestprior = max(largestprior, price)
print(gap)
