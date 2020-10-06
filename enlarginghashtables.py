p = [True for i in range(46500)]
p[0], p[1] = False, False
for i in range(2, 46500):
    if p[i]:
        for x in range(i*i, 46500, i):
            p[x] = False
primes = set()
listprimes = []
for i in range(2, 46500):
    if p[i]:
        primes.add(i)
        listprimes.append(i)

n = int(input())
while n > 0:
    nisprime = True
    if n not in primes:
        for p in listprimes:
            if n % p == 0:
                nisprime = False
                break

    x = 2*n - 1
    xisprime = False
    while not xisprime:
        x += 2
        if x in primes:
            xisprime = True
        else:
            for p in listprimes:
                if x % p == 0:
                    break
            if x % p != 0:
                xisprime = True

    if nisprime:
        print(x)
    else:
        print(x, f'({n} is not prime)')
        
    n = int(input())
