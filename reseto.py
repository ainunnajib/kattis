n, k = map(int, input().split())
i = 2
crossed = set()
while k > 0:
    x = i
    while x <= n:
        if x not in crossed:
            crossed.add(x)
            k -= 1
            if k == 0:
                print(x)
                break
        x += i

    while i in crossed:
        i += 1
