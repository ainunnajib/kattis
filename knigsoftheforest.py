from collections import defaultdict
import heapq

k, n = map(int, input().split())
d = defaultdict(list)
karly, karls = map(int, input().split())
d[karly].append(-1*karls)
for _ in range(n+k-2):
    y, s = map(int, input().split())
    d[y].append(-1*s)

unknown = True
l = []
for x in sorted(d.keys()):
    for y in d[x]:
        if len(l) == k:
            heapq.heappop(l)
        heapq.heappush(l, y)

    if l[0] == -1*karls and x >= karly:
        print(x)
        unknown = False
        break
if unknown:
    print('unknown')
