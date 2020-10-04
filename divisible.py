c = int(input())
for _ in range(c):
    d, n = map(int, input().split())
    l = list(map(int, input().split()))

    ans = 0
    sum = 0
    mod = [0 for m in range(d)]
    for i in range(n):
        sum += l[i]
        ans += mod[sum%d]
        if sum%d == 0:
            ans += 1
        mod[sum%d] += 1
    print(ans)
