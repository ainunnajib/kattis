from collections import defaultdict
from math import *
from sys import stdin, stdout

p = [True for i in range(46350)]
p[0], p[1] = False, False
for i in range(2, 46350):
    if p[i]:
        for x in range(i*i, 46350, i):
            p[x] = False
primes = set()
listprimes = []
for i in range(2, 46350):
    if p[i]:
        primes.add(i)
        listprimes.append(i)

for line in stdin.readlines():
    n, m = map(int, line.split())
    if m == 0:
        stdout.write(f'0 does not divide {n}!\n')
        continue
    if n == 0:
        if m == 1:
            stdout.write('1 divides 0!\n')
        else:
            stdout.write(f'{m} does not divide {n}!\n')
        continue

    factors = defaultdict(int)
    x = m
    enough = True
    for p in listprimes:
        if p*p > x:
            if n < x:
                enough = False
            break

        s = 0
        while x % p == 0:
            x //= p
            factors[p] += 1
            s += floor(n/(p**factors[p]))
            if s < factors[p]:
                enough = False
                break
        if x == 1:
            break

    if enough:
        stdout.write(f'{m} divides {n}!\n')
    else:
        stdout.write(f'{m} does not divide {n}!\n')
