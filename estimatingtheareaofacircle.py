import math
r, m, c = map(float, input().split())
while r != 0 or m != 0 or c != 0:
    print(math.pi*r*r, 4*r*r*c/m)
    r, m, c = map(float, input().split())
