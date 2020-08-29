import math
s = input()
while s != '0':
    x, y, a, b, p = map(float, s.split())
    print(math.pow(math.pow(abs(x-a), p) + math.pow(abs(y-b), p), 1/p))
    s = input()
