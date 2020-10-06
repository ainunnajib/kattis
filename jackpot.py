n = int(input())
for _ in range(n):
    done = False
    w = int(input())
    l = list(map(int, input().split()))
    ans = l[0]
    for n in l[1:]:
        x, y = ans, n
        while y > 0:
            x, y = y, x%y
        ans *= n // x
        if ans > 1000000000:
            print('More than a billion.')
            done = True
            break

    if not done:
        print(ans)
