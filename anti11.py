mod = 1000000007
fib = [0 for i in range(10001)]
fib[1], fib[2] = 2, 3
for i in range(3, 10001):
    fib[i] = (fib[i-1] + fib[i-2]) % mod

t = int(input())
for _ in range(t):
    print(fib[int(input())])
