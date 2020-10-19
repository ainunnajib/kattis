import math
from fractions import Fraction

n1, n2 = map(int, input().split())
l1 = list(map(int, input().split()))[::-1]
l2 = list(map(int, input().split()))[::-1]

f1 = Fraction(l1[0], 1)
for x in l1[1:]:
    f1 = x + Fraction(1, f1)

f2 = Fraction(l2[0], 1)
for x in l2[1:]:
    f2 = x + Fraction(1, f2)

res = f1 + f2
ans = []
while True:
    a = math.floor(res)
    ans.append(str(a))
    res -= a
    if res == 0:
        break
    res = Fraction(1, res)
print(' '.join(ans))

res = f1 - f2
ans = []
while True:
    a = math.floor(res)
    ans.append(str(a))
    res -= a
    if res == 0:
        break
    res = Fraction(1, res)
print(' '.join(ans))

res = f1 * f2
ans = []
while True:
    a = math.floor(res)
    ans.append(str(a))
    res -= a
    if res == 0:
        break
    res = Fraction(1, res)
print(' '.join(ans))

res = f1 / f2
ans = []
while True:
    a = math.floor(res)
    ans.append(str(a))
    res -= a
    if res == 0:
        break
    res = Fraction(1, res)
print(' '.join(ans))
