n = int(input())
l = list(map(int, input().split()))
l.sort()
a, b = map(int, input().split())

maxdist = 0

x = a
if x%2 == 0:
    x += 1
mindist = abs(l[0] - x)
for y in l[1:]:
    if mindist > abs(y - x):
        mindist = abs(y - x)
maxdist = mindist
ans = x

x = b
if x%2 == 0:
    x -= 1
mindist = abs(l[0] - x)
for y in l[1:]:
    if mindist > abs(y - x):
        mindist = abs(y - x)
if maxdist < mindist:
    maxdist = mindist
    ans = x

for i in range(n-1):
    x = (l[i]+l[i+1])//2
    if x%2 == 0:
        x += 1
    if x >= a and x <= b:
        if maxdist < abs(l[i+1]-x):
            maxdist = abs(l[i+1]-x)
            ans = x

print(ans)
