n, m = map(int, input().split())
missing = [True for _ in range(n+1)]
l = []
for _ in range(m):
    x = int(input())
    l.append(x)
    missing[x] = False

appendall = False
i = 0
for x in range(1, n+1):
    if missing[x]:
        if appendall:
            l.append(x)
        else:
            while l[i] < x:
                i += 1
                if i == len(l):
                    appendall = True
                    break
            if appendall:
                l.append(x)
            else:
                l.insert(i, x)
for x in l:
    print(x)
