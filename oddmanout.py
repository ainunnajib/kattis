from collections import defaultdict
n = int(input())
for i in range(n):
    g = int(input())
    l = input().split()
    d = defaultdict(int)
    for c in l:
        d[c] += 1
    for k, v in d.items():
        if v == 1:
            print("Case #" + str(i+1) + ": " + k)
            break