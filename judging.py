from collections import defaultdict
n = int(input())
d1 = defaultdict(int)
for _ in range(n):
    d1[input()] += 1
d2 = defaultdict(int)
for _ in range(n):
    d2[input()] += 1
count = 0
for k in d1:
    count += min(d1[k], d2[k])
print(count)
