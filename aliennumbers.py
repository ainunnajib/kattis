t = int(input())
for i in range(1, t+1):
    numfrom, xfrom, xto = input().split()
    basefrom = len(xfrom)
    baseto = len(xto)
    n = 0
    x = 1
    for c in numfrom[::-1]:
        n += xfrom.index(c) * x
        x *= basefrom
    r = ''
    while n > 0:
        r = xto[n%baseto] + r
        n //= baseto
    print('Case #' + str(i) + ':', r)
