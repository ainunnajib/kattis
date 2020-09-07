from itertools import combinations_with_replacement
from collections import defaultdict

n = int(input())
pd = defaultdict(int)
while n%2 == 0:
    n //= 2
    pd[2] += 1
for x in range(3, 33000000, 2):
    while n%x == 0:
        n //= x
        pd[x] +=1
    if n == 1:
        break

k = 0
tuples = {}
for c in range(1, 61):
    sortedprimes = sorted(pd.keys())
    for pp in combinations_with_replacement(sortedprimes, c):
        t = tuple(sorted(list(pp)))
        can = True
        buffer = defaultdict(int)
        for x in t:
            if x not in pd:
                can = False
            elif x not in buffer:
                buffer[x] = pd[x]
            buffer[x] -= 1
        if min(buffer.values()) < 0:
            can = False
        if can:
            for x in t:
                pd[x] -= 1
                if pd[x] == 0:
                    pd.pop(x, None)
            tuples[t] = True
        if len(pd) == 0:
            break
    if len(pd) == 0:
        break

print(len(tuples))
