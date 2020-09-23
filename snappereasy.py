t = int(input())
for c in range(1, t+1):
    n, k = map(int, input().split())
    print('Case #' + str(c) + ':', 'ON' if (k+1)%(2**n) == 0 else 'OFF')
