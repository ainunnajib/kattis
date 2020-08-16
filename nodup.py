from collections import defaultdict
d = defaultdict(int)
s = input().split()
for ss in s:
    d[ss] += 1
if max(d.values()) > 1:
    print("no")
else:
    print("yes")