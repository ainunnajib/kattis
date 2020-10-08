import sys
from collections import defaultdict

MAX = 46350
p = [True for i in range(MAX)]
p[0], p[1] = False, False
for i in range(2, MAX):
    if p[i]:
        for x in range(i*i, MAX, i):
            p[x] = False
primes = set()
listprimes = []
for i in range(2, MAX):
    if p[i]:
        primes.add(i)
        listprimes.append(i)

for line in sys.stdin.readlines():
    n = int(line)
    negative = n < 0
    n = abs(n)

    factors = defaultdict(int)
    for p in listprimes:
        if p*p > n:
            break
        while n % p == 0:
            n //= p
            factors[p] += 1
        if n == 1:
            break
    if n > 1:
        factors[n] += 1

    l = []
    if negative:
        l.append('-1')
    for f in sorted(factors.keys()):
        if factors[f] == 1:
            l.append(str(f))
        else:
            l.append(str(f)+'^'+str(factors[f]))

    print(' '.join(l))
