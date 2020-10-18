l, d, n = map(int, input().split())
l -= 12
birds = []
for _ in range(n):
    birds.append(int(input()) - 6)
birds.sort()

if l < 0:
    print(0)
elif n == 0:
    print(l//d + 1)
else:

    if birds[0] >= d:
        count = 1
    else:
        count = 0
    cur = 0
    for b in birds:
        slots = (b-cur)//d - 1
        if slots > 0:
            count += slots
        cur = b
    slots = (l-cur)//d
    if slots > 0:
        count += slots

    print(count)
