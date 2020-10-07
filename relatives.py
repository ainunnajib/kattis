p = [True for i in range(32000)]
p[0], p[1] = False, False
for i in range(2, 32000):
    if p[i]:
        for x in range(i*i, 32000, i):
            p[x] = False
primes = set()
listprimes = []
for i in range(2, 32000):
    if p[i]:
        primes.add(i)
        listprimes.append(i)

n = int(input())
while n > 0:
    ans = n
    for p in listprimes:
        if n % p == 0:
            ans -= ans//p
            while n % p == 0:
                n //= p
    if n > 1:
        ans -= ans//n

    print(ans)

    n = int(input())
