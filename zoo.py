from collections import defaultdict
n = int(input())
t = 1
while n != 0:
    d = defaultdict(int)
    for _ in range(n):
        d[input().split()[-1].lower()] += 1

    l = sorted(d.keys())
    print('List', str(t)+':')
    for x in l:
        print(x, '|', d[x])

    t += 1
    n = int(input())
