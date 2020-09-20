from itertools import permutations
h = list(map(int, input().split()))
b = h.pop()
a = h.pop()
for p in permutations(h):
    x = list(p[:3])
    y = list(p[3:])
    if sum(x) == a and sum(y) == b:
        x.sort(reverse = True)
        y.sort(reverse = True)
        x.extend(y)
        s = [str(i) for i in x]
        print(' '.join(s))
        break
