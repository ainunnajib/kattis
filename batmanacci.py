n, k = map(int, input().split())
fib = [0 for _ in range(n+1)]
fib[0], fib[1], fib[2] = 0, 1, 1
for i in range(3, n+1):
    fib[i] = fib[i-2] + fib[i-1]

while n > 2:
    if k <= fib[n-2]:
        n -= 2
    else:
        k -= fib[n-2]
        n -= 1

print('N' if n == 1 else 'A')