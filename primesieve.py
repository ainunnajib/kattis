n, q = map(int, input().split())
isprime = [True] * (n+1)
isprime[0] = False
isprime[1] = False
for i in range(2,n+1):
    if isprime[i]:
        x = 2*i
        while x <= n:
            isprime[x] = False
            x += i
print(sum(isprime))
for _ in range(q):
    print(int(isprime[int(input())]))
