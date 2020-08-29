import math
a, b = map(int, input().split('/'))
a -= b*32
a *= 5
b *= 9
f = math.gcd(a, b)
a //= f
b //= f
if b < 0:
    a *= -1
    b *= -1
print(f'{a}/{b}')
