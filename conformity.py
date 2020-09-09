from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n):
    s = input().split()
    s.sort()
    s = ''.join(s)
    d[s] += 1
maxd = max(d.values())
total = 0
for x in d.values():
    if x == maxd:
        total += x
print(total)
