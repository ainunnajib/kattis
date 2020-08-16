from collections import defaultdict
n = int(input())
t = int(input())
d = {}
for i in range(t):
    s = input().split()
    d[s[0]] = s[2]
    d[s[1]] = s[3]
    if s[2] == s[3]:
        d.pop(s[0])
        d.pop(s[1])
        n -= 2
dd = defaultdict(int)
for k, v in d.items():
    dd[v] += 1
double = 0
single = 0
for k, v in dd.items():
    if v == 2:
        double += 1
    elif v == 1:
        single += 1
known = single + double
if n == 2*known:
    double += single
if n == 2*double + 2:
    double += 1
print(double)