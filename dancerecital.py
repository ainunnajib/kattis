from itertools import permutations
r = int(input())
l = []
for _ in range(r):
    l.append(set(input()))

d = {}
for i in range(r):
    for j in range(i+1, r):
        x = len(l[i] & l[j])
        d[(i, j)] = x
        d[(j, i)] = x

minq = 26 * r
for t in permutations(range(r)):
    q = 0
    for i in range(r-1):
        q += d[(t[i], t[i+1])]
    minq = min(minq, q)

print(minq)
