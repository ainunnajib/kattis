from collections import defaultdict
n, t = map(int, input().split())
a = list(map(int, input().split()))
if t == 1:
    d = {}
    found = False
    for x in a:
        if (7777-x) in d:
            print('Yes')
            found = True
            break
        else:
            d[x] = True
    if not found:
        print('No')
elif t == 2:
    a.sort()
    unique = True
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('Contains duplicate')
            unique = False
            break
    if unique:
        print('Unique')
elif t == 3:
    d = defaultdict(int)
    maxnum = 0
    thenum = -1
    for x in a:
        d[x] += 1
        if maxnum < d[x]:
            maxnum = d[x]
            thenum = x
    if maxnum*2 > n:
        print(thenum)
    else:
        print(-1)
elif t == 4:
    a.sort()
    if n%2 == 1:
        print(a[n//2])
    else:
        print(a[n//2-1], a[n//2])
elif t == 5:
    a.sort()
    s = []
    for x in a:
        if x >= 100 and x <= 999:
            s.append(str(x))
    print(' '.join(s))
