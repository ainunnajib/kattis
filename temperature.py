x, y = map(int, input().split())
#B = yA + x --> A = B = x/(1-y)
if y == 1:
    if x == 0:
        print("ALL GOOD")
    else:
        print("IMPOSSIBLE")
else:
    print(x/(1-y))