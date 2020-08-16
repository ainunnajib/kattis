from math import *
n = int(input())
for x in range(n):
    s = input()
    r = ""
    k = int(sqrt(len(s)))
    for j in range(k-1,-1,-1):
        for i in range(k):
            r += s[i*k+j]
    print(r)