import math
n = int(input())
for _ in range(n):
    s = input()
    l = len(s)
    k = int(math.ceil(math.sqrt(l)))
    for i in range(k*k-l):
        s += '*'
    a = []
    for i in range(k):
        a.append(s[i*k:(i+1)*k])
    b = []
    for j in range(k):
        r = ""
        for i in range(k-1,-1,-1):
            if a[i][j] != '*':
                r += a[i][j]
        b.append(r)
    print(''.join(b))
