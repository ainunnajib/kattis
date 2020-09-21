t = int(input())
for case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse = True)
    scalar = sum([a[i]*b[i] for i in range(n)])
    print('Case #' + str(case) + ':', scalar)
