import math
x = input()
l = len(x)
if x == '1':
    print(1)
elif l < 10:
    x = int(x)
    n = 0
    while x > 1:
        n += 1
        x /= n
    print(n)
else:
    n = 0
    s = 0
    while math.floor(s) + 1 < l:
        n += 1
        s += math.log10(n)
    print(n)
