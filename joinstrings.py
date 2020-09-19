import sys
inputs = iter(sys.stdin.readlines())
n = int(next(inputs))
l = ['']
for _ in range(n):
    l.append(next(inputs).strip())
a, b = 1, 1
d = {1:[1]}
for _ in range(n-1):
    a, b = map(int, next(inputs).split())
    if a in d and b in d:
        d[a].extend(d[b])
    elif a in d:
        d[a].append(b)
    elif b in d:
        d[a] = [a]
        d[a].extend(d[b])
    else:
        d[a] = [a, b]
for i in d[a]:
    sys.stdout.write(l[i])
