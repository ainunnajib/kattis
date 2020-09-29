prime = [True for i in range(1000000)]
prime[0] = False
prime[1] = False
for p in range(2, 1000000):
    if prime[p]:
        for i in range(p*p, 1000000, p):
            prime[i] = False

primes = set()
for p in range(1000000):
    if prime[p]:
        primes.add(p)

def isprime(p):
    if p in primes:
        return True
    else:
        for x in primes:
            if p%x == 0:
                return False
        primes.add(p)
        return True

n, b = map(int, input().split())

if n >= b and n > 2:
    print('impossible')
elif n == 2:
    print('1 2')
    print('2 1')
else:
    a = list(range(1, n+1))
    suma = sum(a)
    addition = 0
    while not isprime(suma+addition):
        addition += 1
    if (n*(b + b-n+1))//2 < suma + addition:
        print('impossible')
    else:
        i = n-1
        while addition + a[i] > b - (n-1-i):
            addition -= (b - (n-1-i)) - a[i]
            a[i] = b - (n-1-i)
            i -= 1
        a[i] += addition

        s = [str(x) for x in a]
        for i in range(n):
            l = s[i:] + s[:i]
            print(' '.join(l))
