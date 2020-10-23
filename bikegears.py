from fractions import Fraction

nf, nb = map(int, input().split())
lf = list(map(int, input().split()))
lb = list(map(int, input().split()))

l = []
for f in lf:
    for b in lb:
        l.append((Fraction(f, b), f, b))
l.sort()
for _, f, b in l:
    print('(' + str(f) + ',' + str(b) + ')')
