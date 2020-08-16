from collections import defaultdict
n = int(input())
for i in range(n):
    d = defaultdict(int)
    k = int(input())
    for j in range(k):
        d[input()] += 1
    print(len(d))