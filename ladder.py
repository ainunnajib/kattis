from math import *
l = input().split()
h = float(l[0])
v = float(l[1])
print(int(ceil(h/sin(radians(v)))))