import math
n, k = map(int, input().split())
d = 0
while n > 0:
    n -= math.ceil(n/k)
    d += 1
d += 1
print(d)
