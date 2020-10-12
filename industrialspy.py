from itertools import permutations
from collections import defaultdict

MAX = 10000000
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
        
t = int(input())
for _ in range(t):
    d = list(input())
    ld = len(d)
    
    done = set()
    count = 0
    for i in range(1, ld+1):
        for x in permutations(d, i):
            p = int(''.join(x))
            if p not in done and p in primes:
                count += 1
                done.add(p)
    
    print(count)
