from collections import defaultdict
d = defaultdict(int)

s = input()
n = len(s)

for c in s:
    d[c] += 1
odd = 0
for x in d.values():
    if x%2 == 1:
        odd += 1
print(max(odd-1, 0))
