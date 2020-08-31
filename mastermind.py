from collections import defaultdict
s = input().split()
n = int(s[0])
a = s[1]
b = s[2]
r = 0
s = 0
da = defaultdict(int)
db = defaultdict(int)
for i in range(n):
    if a[i] == b[i]:
        r += 1
    else:
        da[a[i]] += 1
        db[b[i]] += 1
s = 0
for x in da:
    s += min(da[x], db[x])
print(r, s)
