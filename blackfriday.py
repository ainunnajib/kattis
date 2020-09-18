from collections import defaultdict
n = int(input())
q = list(map(int, input().split()))
d = defaultdict(int)
l = []
for i in range(n):
    l.append((q[i], i+1))
    d[q[i]] += 1
l.sort(reverse = True)
printed = False
for x in l:
    if d[x[0]] == 1:
        print(x[1])
        printed = True
        break
if not printed:
    print('none')
