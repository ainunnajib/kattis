l, n = map(int, input().split())
k = 1
while l%n != 0:
    n = n - l%n
    k += 1
print(k)
