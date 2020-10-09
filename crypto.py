from collections import defaultdict

MAX = 1000000
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

n = int(input())
f = defaultdict(int)
for p in listprimes:
    while n % p == 0:
        f[p] += 1
        n //= p

ans = n
maxzeros = 0
for k in sorted(f.keys()):
    if f[k] > maxzeros:
        ans = k
        maxzeros = f[k]
print(ans)
