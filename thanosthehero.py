n = int(input())
l = list(map(int, input().split()))
l = l[::-1]
x = l[0]
kill = 0
possible = True
for y in l[1:]:
    if x == 0:
        possible = False
        break
    if y >= x:
        kill += y - x + 1
        x = x - 1
    else:
        x = y
if not possible:
    print(1)
else:
    print(kill)
