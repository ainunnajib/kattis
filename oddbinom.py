import math
global a
a = {1:1}

def f(x):
    if x in a:
        return a[x]
    a[x] = 2 * f(math.floor(x/2)) + f(math.ceil(x/2))
    return a[x]

n = int(input())
print(f(n))
