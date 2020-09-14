from decimal import Decimal
n, m, p = map(int, input().split())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
l = []
for x in c:
    for y in d:
        l.append(Decimal(x/y))
l.sort()
okay = True
for i in range(len(l)-1):
    if l[i+1]/l[i] > Decimal(1 + p/100):
        okay = False
        break
if okay:
    print('Ride on!')
else:
    print('Time to change gears!')
