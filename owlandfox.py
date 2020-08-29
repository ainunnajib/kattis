n = int(input())
for _ in range(n):
    x = int(input())
    sumx = sum([int(i) for i in str(x)])
    sumy = -2
    y = x
    while sumy != sumx - 1 and y > 0:
        y -= 1
        sumy = sum([int(i) for i in str(y)])
    print(y)
