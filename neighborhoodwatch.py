n, k = map(int, input().split())
s = set()
for _ in range(k):
    s.add(int(input()))
x = 0
unsafe = 0
for i in range(1, n+1):
    if i in s:
        unsafe += x*(x-1)//2 + x
        x = 0
    else:
        x += 1
unsafe += x*(x-1)//2 + x

print(n*(n-1)//2 + n - unsafe)
