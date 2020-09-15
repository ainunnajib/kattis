n, p = map(int, input().split())
a = list(map(int, input().split()))
a = [x-p for x in a]
m = [0 for _ in range(n)]
m[0] = a[0]
maxval = a[0]
for i in range(1, n):
    m[i] = max(m[i-1], 0) + a[i]
    maxval = max(maxval, m[i])
print(maxval)
