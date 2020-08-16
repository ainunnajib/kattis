from math import *
n = int(input())
for i in range(n):
    l = input().split()
    v = float(l[0])
    theta = float(l[1])
    x = float(l[2])
    h1 = float(l[3]) + 1
    h2 = float(l[4]) - 1
    t = x/v/cos(radians(theta))
    y = x*tan(radians(theta)) - 0.5*9.81*t*t 
    if y > h1 and y < h2:
        print("Safe")
    else:
        print("Not Safe")