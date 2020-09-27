n = int(input())
l = []
i = 0
while (i+1)**2 < n:
    if n%(i+1) == 0:
        l.append(i)
        l.append(n//(i+1) - 1)
    i += 1
if (i+1)**2 == n:
    l.append(i)
l.sort()
s = [str(x) for x in l]
print(' '.join(s))
