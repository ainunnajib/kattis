n = int(input())
while n > 0:
    l = []
    for i in range(n):
        x, y = map(int, input().split())
        l.append((x, y))
        if i == n//2:
            centre = (x, y)

    s, o = 0, 0
    for x, y in l:
        if (x > centre[0] and y > centre[1]) or (x < centre[0] and y < centre[1]):
            s += 1
        elif (x > centre[0] and y < centre[1]) or (x < centre[0] and y > centre[1]):
            o += 1

    print(s, o)

    n = int(input())
