import math
n, k = map(int, input().split())
a = [0 for i in range(100001)]
for _ in range(n):
    x = int(input())
    for i in range(x, min(x+1000, 100001)):
        a[i] += 1
print(math.ceil(max(a)/k))
