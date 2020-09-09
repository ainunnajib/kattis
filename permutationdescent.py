a = [[-1 for i in range(1001)] for j in range(1001)]
a[0][0] = 0
for n in range(1, 1001):
    a[n][0] = 1
    a[n][n] = 0
    a[n][n-1] = 1

def pdc(n, k):
    if a[n][k] != -1:
        return a[n][k]
    a[n][k] = (k+1) * pdc(n-1, k) + (n-k) * pdc(n-1, k-1)
    return a[n][k]

p = int(input())
for _ in range(p):
    k, n, v = map(int, input().split())
    print(k, pdc(n, v)%1001113)
