p = int(input())
for _ in range(p):
    k, n = map(int, input().split())
    l = []
    while len(l) < n:
        l.extend(list(map(int, input().split())))

    s = sorted(l)
    count = 0
    i = 0
    for x in l:
        if x == s[i]:
            i += 1
        else:
            count += 1

    print(k, count)
