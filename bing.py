from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n):
    w = input()
    print(d[w])
    for i in range(1, len(w)+1):
        d[w[:i]] += 1
