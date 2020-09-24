p = [True for i in range(10001)]
p[0], p[1] = False, False
for i in range(2, 10001):
    if p[i]:
        for j in range(i*i, 10001, i):
            p[j] = False
primes = set()
for i in range(2, 10001):
    if p[i]:
        primes.add(i)

t = int(input())
for _ in range(t):
    case, m = map(int, input().split())
    happy = False
    if m in primes:
        s = str(m)
        x = 0
        for c in s:
            x += int(c)**2
        cycle = set()
        cycle.add(1)
        cycle.add(m)
        while x not in cycle:
            cycle.add(x)
            s = str(x)
            x = 0
            for c in s:
                x += int(c)**2
        if x == 1:
            happy = True
    print(case, m, 'YES' if happy else 'NO')
