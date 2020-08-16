from math import *
s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
s = 1.0*(a+b+c+d)/2
print(sqrt((s-a)*(s-b)*(s-c)*(s-d)))