s, v1, v2 = map(int, input().split())
c1 = s//v1
s -= c1*v1
c2 = s//v2
s -= c2*v2
while s%v2 != 0:
    s += v1
    c1 -= 1
c2 += s//v2
if c1 >= 0:
    print(c1, c2)
else:
    print("Impossible")
