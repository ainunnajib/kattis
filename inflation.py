n = int(input())
c = list(map(int, input().split()))
c.sort()
minfrac = 1.0
impossible = False
for i in range(1, n+1):
    if i < c[i-1]:
        impossible = True
        break
    frac = 1.0*c[i-1]/i
    minfrac = min(minfrac, frac)
if impossible:
    print('impossible')
else:
    print(minfrac)
