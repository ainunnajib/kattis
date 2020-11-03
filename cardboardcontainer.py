import math
v = int(input())

minsurface = 6*v
for a in range(1, math.floor(math.sqrt(v))+1):
    for b in range(1, math.floor(math.sqrt(v))+1):
        if v % (a*b) == 0:
            c = v // (a*b)
            surface = 2 * (a*b + b*c + c*a)
            minsurface = min(minsurface, surface)
print(minsurface)
