from math import *
def dist(a, b):
    xa = int(a/3)
    ya = int(a%3)
    xb = int(b/3)
    yb = int(b%3)
    dx = xa-xb
    dy = ya-yb
    return 1.0*sqrt(dx*dx+dy*dy)

seq = ""
for i in range(3):
    s = input().split()
    for c in s:
        seq += c
total = 0.0
abc = '123456789'
for i in range(8):
    total += dist(seq.index(abc[i]),seq.index(abc[i+1]))
print(total)