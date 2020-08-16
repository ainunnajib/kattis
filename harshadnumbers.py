def sumdigits(x):
    s = 0
    while x > 0:
        s += x%10
        x = int(x/10)
    return s

n = int(input())
while True:
    k = sumdigits(n)
    if n%k == 0:
        print(n)
        break
    n += 1