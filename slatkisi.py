c, k = map(int, input().split())
x = c
for _ in range(k):
    x //= 10
for _ in range(k):
    x *= 10
if 10**k + x - c <= c - x:
    x += 10**k
print(x)
