from itertools import permutations
s = input()
n = int(s)
s = list(s)
l = []
for p in permutations(s):
    l.append(int(''.join(p)))
l.sort()
i = l.index(n)
while i < len(l) - 1:
    if l[i+1] > l[i]:
        break
    i += 1
i += 1
if i == len(l):
    print(0)
else:
    print(l[i])
