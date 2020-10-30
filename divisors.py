from collections import defaultdict

MAX = 432
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

primefactors = [defaultdict(int) for _ in range(MAX)]
for n in range(2, MAX):
    x = n
    for p in listprimes:
        while x % p == 0:
            x //= p
            primefactors[n][p] += 1
        if x == 1:
            break

while True:
    try:
        n, k = map(int, input().split())

        factors = defaultdict(int)
        for i in range(n, n-k, -1):
            for p in primefactors[i]:
                factors[p] += primefactors[i][p]

        for i in range(2, k+1):
            for p in primefactors[i]:
                factors[p] -= primefactors[i][p]

        ans = 1
        for p in factors:
            if factors[p] > 0:
                ans *= (factors[p] + 1)

        print(ans)
    except EOFError:
        break
