n, c = map(int, input().split())
l = list(map(int, input().split()))
maxcount = 0
for i in range(n):
    total = 0
    count = 0
    for j in range(i, n):
        if total + l[j] <= c:
            total += l[j]
            count += 1
        if total == c:
            break
    maxcount = max(maxcount, count)
print(maxcount)
