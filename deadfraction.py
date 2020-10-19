import math
from fractions import Fraction

s = input()
while s != '0':
    s = s[2:-3]
    l = len(s)
    r = int(s)
    ans = Fraction(r, 10**l - 1)

    for i in range(1, l):
        f = int(s[:-1*i])
        r = int(s[-1*i:])
        num = f*(10**i - 1) + r
        denom = 10**l - 10**(l-i)
        f = Fraction(num, denom)
        if ans.denominator > f.denominator:
            ans = f

    if math.floor(ans) == ans:
        print(str(int(ans)) + '/1')
    else:
        print(ans)

    s = input()
