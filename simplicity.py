from collections import defaultdict
d = defaultdict(int)
s = input()
for c in s:
    d[c] += 1
v = sorted(d.values())
print(sum(v[:-2]))
