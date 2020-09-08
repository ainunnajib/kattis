import sys
import math
l = sys.stdin.readlines()[0].strip()
k = len(l)
k -= 1
l = int(l)

if k > 10**1000:
    print(0)
elif k > 0:
    n = math.ceil((10**k)/k)
    d = len(str(n))
    n += (l-n*d)//d
    while n * len(str(n)) > l and limit > 0:
        n -= 1
    print(n)
else:
    print(l)

#while k > 0:
#    if l%k != 0:
#        k -= 1
#    elif len(str(l//k)) * (l//k) == l:
#        break
#    else:
#        k -= 1
#if k > 0:
#    print(l//k)

#minnum = {}
#maxnum = {}
#LIMIT = 10000000
#for i in range(1, LIMIT+1):
#    x = len(str(i * len(str(i))))
#    if x not in minnum:
#        minnum[x] = i
#    maxnum[x] = i
#
#for k in minnum:
#    print(k, minnum[k], maxnum[k])
