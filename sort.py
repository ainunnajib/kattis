from collections import defaultdict
n, c = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)
for x in a:
    d[x] += 1
l = []
done = {}
for x in sorted(d.values(), reverse = True):
    if x not in done:
        for k in d:
            if d[k] == x:
                for _ in range(x):
                    l.append(str(k))
    done[x] = True
print(' '.join(l))
