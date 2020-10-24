from fractions import Fraction
m, n = map(int, input().split())
t = list(map(int, input().split()))
x = list(map(int, input().split()))

l = [t[i+1] - t[i] for i in range(m-1)]
s = [x[i+1] - x[i] for i in range(n-1)]

dists = set()
for i in range(n-m+1):
    f = Fraction(s[i], l[0])
    valid = True
    for j in range(1, m-1):
        if Fraction(s[i+j], l[j]) != f:
            valid = False
            break
    if valid:
        dists.add(s[i])

print(len(dists))
print(' '.join([str(c) for c in sorted(dists)]))
