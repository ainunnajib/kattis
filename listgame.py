n = int(input())
result = 0
k = 2
while n > 1:
    if k*k > n:
        result += 1
        break
    while n%k == 0:
        result += 1
        n = int(n/k)
    k += 1
print(result)