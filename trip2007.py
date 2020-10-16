from collections import defaultdict

n = int(input())
while n > 0:
    l = []
    while len(l) < n:
        l.extend(list(map(int, input().split())))
    l.sort()

    d = defaultdict(int)
    for x in l:
        d[x] += 1

    k = max(d.values())
    ans = [[] for _ in range(k)]
    i = 0
    for x in l:
        ans[i].append(str(x))
        i += 1
        i %= k

    print(k)
    for a in ans:
        print(' '.join(a))
    
    n = int(input())
