t = int(input())
for _ in range(t):
    m = int(input())
    a = list(map(int, input().split()))
    n = int(input())
    b = list(map(int, input().split()))
    c = [0 for i in range(m+n+1)]
    for i in range(m+1):
        for j in range(n+1):
            c[i+j] += a[i]*b[j]
    print(m+n)
    cs = [str(x) for x in c]
    print(' '.join(cs))
