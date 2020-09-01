n = int(input())
for t in range(n):
    s = int(input())
    a = input().split()
    b, r = [], []
    for x in a:
        if x[-1] == 'B':
            b.append(int(x[:-1]))
        elif x[-1] == 'R':
            r.append(int(x[:-1]))
    b.sort()
    b = b[::-1]
    r.sort()
    r = r[::-1]
    l = min(len(b), len(r))
    length = 0
    for j in range(l):
        length += b[j] + r[j] - 2
    print('Case #'+str(t+1)+':', length)
