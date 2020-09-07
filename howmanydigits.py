import sys
import math

ans = [0 for i in range(1000001)]
ans[0] = 1
l = 0
for n in range(1, 1000001):
    l += math.log10(n)
    ans[n] = int(math.floor(l) + 1)

for line in sys.stdin.readlines():
    n = int(line)
    print(ans[n])
