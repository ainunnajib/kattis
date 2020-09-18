p = [True for i in range(32001)]
p[0] = False
p[1] = False
for i in range(2, 180):
    if p[i]:
        for x in range(i*i, 32001, i):
            p[x] = False
primes = [i for i in range(2, 32001) if p[i]]
setprimes = set(primes)

t = int(input())
for _ in range(t):
    n = int(input())

    l = []
    for p in primes:
        if p+p > n:
            break
        if p+p == n:
            l.append((p, p))
            break
        if (n-p) in setprimes:
            l.append((p, n-p))

    print(n, 'has', len(l), 'representation(s)')
    for t in l:
        print(str(t[0]) + '+' + str(t[1]))
    print()
