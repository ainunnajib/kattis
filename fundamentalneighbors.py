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
    x = n
    factors = defaultdict(int)
    for p in listprimes:
        if p*p > x:
            break
        while x % p == 0:
            factors[p] += 1
            x //= p
        if x == 1:
            break
    if x > 1:
        factors[x] += 1

    ans = 1
    for p in factors:
        ans *= factors[p] ** p

    print(n, ans)
