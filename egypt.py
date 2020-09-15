n = list(map(int, input().split()))
while sum(n) > 0:
    c = max(n)
    a = min(n)
    b = sum(n) - c - a
    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')

    n = list(map(int, input().split()))
