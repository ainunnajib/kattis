from math import *
s = input().split()
x = int(s[0])
y = int(s[1])
x1 = int(s[2])
y1 = int(s[3])
x2 = int(s[4])
y2 = int(s[5])
x1 -= x
x2 -= x
y1 -= y
y2 -= y
#normalized to (0,0)
dist = 0.0
if (x1 >= 0 and x2 <= 0) or (x1 <= 0 and x2 >= 0):
    dist = min(abs(y1),abs(y2))
elif (y1 >= 0 and y2 <= 0) or (y1 <= 0 and y2 >= 0):
    dist = min(abs(x1),abs(x2))
else:
    x = min(abs(x1),abs(x2))
    y = min(abs(y1),abs(y2))
    dist = sqrt(x*x+y*y)
print(dist)