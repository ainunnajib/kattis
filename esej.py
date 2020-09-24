from itertools import combinations
from random import randint, choice
alphabet = list('abcdefghijklmnopqrstuvwxyz')
a, b = map(int, input().split())
d = []
iter = combinations(alphabet, 15)
while len(d) < b//2 + 1:
    s = ''.join(next(iter))
    d.append(s)

ld = len(d)
l = d.copy()
while len(l) < a:
    l.append(d[randint(0, ld-1)])
if len(l) > b:
    l = l[:b]

print(' '.join(l))
