n, q = map(int, input().split())
#converting N to N//2 instead for space optimization
isprime = [True] * (n//2+1)
isprime[0] = False # N = 1 is not prime
isprime[1] = True # N = 2, 3 are both prime
for i in range(2,n+1):
    if i%2 == 0 and i > 2:
        continue
    if isprime[i//2]:
        x = i*i
        while x <= n:
            if x%2 == 1:
                isprime[x//2] = False
            x += i
print(sum(isprime)+1)
for _ in range(q):
    x = int(input())
    print(0 if x%2 == 0 and x > 2 else int(isprime[x//2]))
