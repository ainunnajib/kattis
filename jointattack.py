from fractions import Fraction

n = int(input())
l = list(map(int, input().split()))

f = Fraction(l[-1], 1)
for x in l[:-1][::-1]:
    f = x + Fraction(1, f)

print(f)
