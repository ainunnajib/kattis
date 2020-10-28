import math
n, p = map(int, input().split())
l = list(map(int, input().split()))
suml = sum(l)
# suml + 100x >= p * (n+x)
# suml + 100x >= pn + px
# x(100-p) >= pn - suml

if p == 100 and p * n > suml:
    print('impossible')
else:
    print(math.ceil((p*n - suml)/(100 - p)))
