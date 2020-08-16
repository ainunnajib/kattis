from math import *
l = input().split()
m = int(l[0])
n = int(l[1])
r = float(l[2])
step = r/n

l = input().split()
x1 = int(l[0])
y1 = int(l[1])
x2 = int(l[2])
y2 = int(l[3])

dist = abs(y2-y1)*step + min(y1,y2)*step*pi*(abs(x2-x1))/m
dist = min(dist, (y1+y2)*step)
print(dist)