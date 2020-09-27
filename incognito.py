from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())

    d = defaultdict(int)
    for __ in range(n):
        a = input().split()
        d[a[1]] += 1

    total = 1
    for k in d:
        total *= d[k] + 1
    total -= 1

    print(total)
