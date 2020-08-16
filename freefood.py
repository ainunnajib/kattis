from collections import defaultdict
d = defaultdict(int)
n = int(input())
for i in range(n):
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    for j in range(a, b+1):
        d[j] += 1
print(len(d))