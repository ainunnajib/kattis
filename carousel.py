n, m = map(int, input().split())
while n!= 0 and m!= 0:
    bestv, besta, bestb = 0, 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= m:
            if bestv < a/b or (bestv == a/b and besta < a):
                bestv = a/b
                besta = a
                bestb = b
    if besta > 0:
        print("Buy", besta, "tickets for $" + str(bestb))
    else:
        print("No suitable tickets offered")
    n, m = map(int, input().split())
