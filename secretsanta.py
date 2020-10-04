from math import *
n = int(input())
if n > 10:
    print(1 - 1/e)
else:
    fn = 1
    for i in range(1, n+1):
        fn *= i
    derangement = floor(fn/e + 0.5)
    print(1 - derangement/fn)
