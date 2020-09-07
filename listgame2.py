from itertools import combinations_with_replacement
from collections import defaultdict
isprime = [True for i in range(33000000)]
for i in range(2, 5746):
    for j in range(i*i, 5746, i):
        isprime[j] = False
primes = []
for p in range(2, 33000000):
    if isprime[p]:
        primes.append(p)

n = int(input())
pd = defaultdict(int)
for p in primes:
    while n%p == 0:
        n //= p
        pd[p] += 1
    if n == 1:
        break

k = 0
tuples = {}
for c in range(1, 61):
    sortedprimes = sorted(pd.keys())
    for pp in combinations_with_replacement(sortedprimes, c):
        t = tuple(sorted(list(pp)))
        can = True
        buffer = defaultdict(int)
        for x in t:
            if x not in pd:
                can = False
            elif x not in buffer:
                buffer[x] = pd[x]
            buffer[x] -= 1
        if min(buffer.values()) < 0:
            can = False
        if can:
            for x in t:
                pd[x] -= 1
                if pd[x] == 0:
                    pd.pop(x, None)
            tuples[t] = True
        if len(pd) == 0:
            break
    if len(pd) == 0:
        break

print(len(tuples))
