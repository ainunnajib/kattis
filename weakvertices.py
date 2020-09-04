n = int(input())
while n != -1:
    b = []
    for _ in range(n):
        r = list(map(int, input().split()))
        b.append([x == 1 for x in r])
    d = [False for i in range(n)]
    for j in range(n):
        for i in range(j+1, n):
            for k in range(n):
                if k == i or k == j:
                    continue
                if b[j][i] and b[j][k] and b[k][i]:
                    d[i] = True
                    d[j] = True
                    d[k] = True
    a = []
    for i in range(n):
        if not d[i]:
            a.append(str(i))
    print(' '.join(a))
    n = int(input())
