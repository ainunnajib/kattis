def numdigits(n):
    x = 0
    while n > 0:
        n //= 10
        x += 1
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    m = 11**n
    num2 = 0
    while numdigits(m) > n:
        m //= 11
        m *= 2
        num2 += 1
    primes = ['2' for i in range(num2)] + ['11' for j in range(n-num2)]
    print(' '.join(primes))
