from collections import defaultdict
n = int(input())
s = input().split()
h = [ int(x) for x in s ]
count = 0
arrowheads = defaultdict(int)
for b in h:
    if arrowheads[b+1] > 0:
        arrowheads[b+1] -= 1
    else:
        count += 1
    arrowheads[b] += 1
print(count)