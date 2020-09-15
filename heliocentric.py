t = 0
while True:
    try:
        t += 1
        e, m = map(int, input().split())
        d = (365-e)%365
        while (d+m)%687 != 0:
            d += 365
        print(f'Case {t}: {d}')
    except EOFError:
        break
