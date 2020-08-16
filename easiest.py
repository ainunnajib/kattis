def sumdigits(x):
    total = 0
    while x > 0:
        total += x%10
        x = int(x/10)
    return total

n = int(input())
while n > 0:
    s = sumdigits(n)
    i = 11
    while s != sumdigits(n*i):
        i += 1
    print(i)
    n = int(input())