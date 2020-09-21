t = int(input())
for _ in range(t):
    l = []
    n = int(input())
    consistent = True
    for __ in range(n):
        l.append(input())
    l.sort()
    for i in range(n-1):
        if l[i+1][:len(l[i])] == l[i]:
            consistent = False
            break
    if consistent:
        print('YES')
    else:
        print('NO')
