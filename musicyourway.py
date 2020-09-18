a = input().split()
la = len(a)

l = []
m = int(input())
for i in range(m):
    l.append(('', i, input().split()))

n = int(input())
for _ in range(n):
    x = input()

    lx = []
    ix = a.index(x)
    for i in range(m):
        t = l[i]
        lx.append((t[2][ix], i, t[2]))
    lx.sort()
    l = lx

    print(' '.join(a))
    for t in l:
        print(' '.join(t[2]))
    print()
