import math
a, n = map(float, input().split())
r = math.sqrt(a / math.pi)
print('Diablo is happy!' if n >= 2 * math.pi * r else 'Need more materials!')
