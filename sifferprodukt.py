def multiplydigits(x):
    r = 1
    for c in x:
        if c != '0':
            r *= int(c)
    return r

n = input()
ans = multiplydigits(n)
while ans > 9:
    ans = multiplydigits(str(ans))
print(ans)
