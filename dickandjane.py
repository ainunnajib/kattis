while True:
    try:
        s, p, y, j = map(int, input().split())
        x = j + 12
        x -= p + y
        d = x%3
        x //= 3
        spot = x + y
        puff = x + p
        yertle = x
        if d == 2:
            spot += 1
            puff += 1
        elif d == 1:
            if s + p == y:
                spot += 1
            else:
                puff += 1

        print(spot, puff, yertle)

    except EOFError:
        break
