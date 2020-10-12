n, x = map(int, input().split())
l = list(map(int, input().split()))
if n == 1:
    print(1)
else:
    l.sort()
    i = 0
    while l[i] + l[i+1] <= x:
        i += 1
        if i == n-1:
            break
    print(i+1)
