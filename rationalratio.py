import math
from fractions import Fraction
s, k = input().split()
k = int(k)
r = int(s[-1*k:])
w = s[:-1*k]
d = w[::-1].index('.')
f = int(w.replace('.', ''))

frac = Fraction(r + f*(10**k - 1), 10**d * (10**k - 1))
if math.floor(frac) == frac:
    print(str(int(frac)) + '/1')
else:
    print(frac)
