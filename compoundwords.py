import sys
d = {}
for line in sys.stdin.readlines():
    words = line.split()
    for w in words:
        d[w] = True

l = [w for w in d]
l.sort()
n = len(l)
r = {}
for i in range(n):
    for j in range(n):
        if i != j:
            r[l[i]+l[j]] = True
rl = [w for w in r]
rl.sort()
for x in rl:
    print(x)
