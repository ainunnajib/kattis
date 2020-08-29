import math
p, q, s = map(int, input().split())
print('yes' if p*q//math.gcd(p, q) <= s else 'no')
