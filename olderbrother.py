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

n = int(input())
if n == 1:
    print('no')
else:
    done = False
    for p in listprimes:
        if n % p == 0:
            while n % p == 0:
                n //= p
            if n == 1:
                print('yes')
            else:
                print('no')
            done = True
            break
    if not done:
        print('yes')
