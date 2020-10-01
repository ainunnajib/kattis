m, n = map(int, input().split())

x, y = m, n
while y > 0:
    x, y = y, x%y

m //= x
n //= x

if m%2 == 1 and n%2 == 1:
    print(x)
else:
    print(0)
