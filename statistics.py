case = 0
while True:
    try:
        x = list(map(int, input().split()))
        x.pop(0)
        case += 1
        print("Case " + str(case) + ": " + str(min(x)) + ' ' + str(max(x)) + ' ' + str(max(x)-min(x)))
    except EOFError:
        break
