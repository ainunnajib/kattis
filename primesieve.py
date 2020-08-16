from bitarray import bitarray
n, q = map(int, input().split())
isprime = bitarray(n+1)
isprime.setall(True)
isprime[0] = False
isprime[1] = False
for i in range(2,n+1):
    if isprime[i]:
        x = i*i
        while x <= n:
            isprime[x] = False
            x += i
print(sum(isprime))
for _ in range(q):
    print(int(isprime[int(input())]))
