s, t, n = map(int, input().split())
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

import math
x = s
for i in range(n):
    x += d[i]
    x = math.ceil(x/c[i])*c[i]
    x += b[i]
x += d[-1]
if x <= t:
    print("yes")
else:
    print("no")
