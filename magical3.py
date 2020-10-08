MAX = 46350
p = [True for i in range(MAX)]
p[0], p[1] = False, False
for i in range(2, MAX):
    if p[i]:
        for x in range(i*i, MAX, i):
            p[x] = False
primes = set()
listprimes = []
for i in range(5, MAX):
    if p[i]:
        primes.add(i)
        listprimes.append(i)

n = int(input())
while n > 0:
    n -= 3
    if n < 0 or n == 1 or n == 2 or n == 3:
        print('No such base')
    elif n % 4 == 0:
        print(4)
    elif n % 5 == 0:
        print(5)
    elif n % 6 == 0:
        print(6)
    elif n % 7 == 0:
        print(7)
    elif n % 9 == 0:
        print(9)
    else:
        for p in listprimes:
            if n % p == 0:
                print(p)
                break
        if n % p != 0:
            if n % 2 == 0:
                n //= 2
            if n % 3 == 0:
                n //= 3
            print(n)

    n = int(input())
