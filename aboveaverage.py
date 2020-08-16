c = int(input())
for i in range(c):
    l = input().split()
    n = int(l[0])
    total = 0
    for j in range(1,n+1):
        total += int(l[j])
    count = 0
    for j in range(1,n+1):
        if int(l[j])*n > total:
            count += 1
    r = '%.3f' % round((100.0*count)/n,3)
    print(r+"%")