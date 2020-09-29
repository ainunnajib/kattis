from collections import defaultdict
p = [True for i in range(47000)]
p[0] = False
p[1] = False
for i in range(2, 47000):
    if p[i]:
        for x in range(i*i, 47000, i):
            p[x] = False
primes = set()
for i in range(47000):
    if p[i]:
        primes.add(i)

n = int(input())
while n != 0:
    negative = n < 0
    n = abs(n)

    d = defaultdict(int)
    for p in primes:
        while n%p == 0:
            n //= p
            d[p] += 1
        if n == 1:
            break
    if n > 1:
        d[n] += 1

    factorcounts = list(d.values())

    gcd = factorcounts[0]
    for f in factorcounts[1:]:
        while f > 0:
            gcd, f = f, gcd%f
    if negative:
        while gcd%2 == 0:
            gcd //= 2
    print(gcd)

    n = int(input())
