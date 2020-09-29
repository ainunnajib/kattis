t = int(input())
for _ in range(t):
    a, b, o, c, d = input().split()
    a, b, c, d = map(int, (a, b, c, d))
    num, denum = 1, 1
    if o == '*':
        num = a * c
        denum = b * d
    elif o == '/':
        num = a * d
        denum = b * c
    elif o == '+':
        num = a*d + c*b
        denum = b*d
    elif o == '-':
        num = a*d - c*b
        denum = b*d

    if num < 0 and denum < 0:
        num *= -1
        denum *= -1
    elif num < 0 or denum < 0:
        num = -1*abs(num)
        denum = abs(denum)

    x, y = abs(num), abs(denum)
    while y > 0:
        x, y = y, x % y

    num //= x
    denum //= x

    print(num, '/', denum)
