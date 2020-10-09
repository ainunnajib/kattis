from math import *

n = int(input())
for _ in range(n):
    w, g, h, r = map(int, input().split())

    minlength = sqrt(w**2 + (h-g)**2)
    maxlength = sqrt(w**2 + (h+g-2*r)**2)

    print(minlength, maxlength)
