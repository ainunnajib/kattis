MAX = 32000
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

p, a = map(int, input().split())
while p > 0 and a > 0:
    isprime = True
    if p not in primes:
        for x in listprimes:
            if p % x == 0:
                isprime = False
                break

    if isprime:
        print('no')
    else:
        bits = bin(p)[2:]
        r = 1
        m = a
        for b in bits[::-1]:
            if b == '1':
                r = (r*m)%p
            m = (m*m)%p

        print('yes' if r == a else 'no')
    
    p, a = map(int, input().split())
