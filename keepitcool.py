n, m, s, d = map(int, input().split())
l = list(map(int, input().split()))
if sum(l) < m:
    print('impossible')
else:
    ts = []
    for i in range(s):
        ts.append((l[i], i))
    ts.sort()

    ans = [0 for _ in range(s)]
    colds = 0
    for t in ts:
        x, i = t
        if n == 0:
            colds += x
            continue
        k = min(n, d-x)
        ans[i] = k
        n -= k

    if colds >= m:
        print(' '.join([str(x) for x in ans]))
    else:
        print('impossible')
