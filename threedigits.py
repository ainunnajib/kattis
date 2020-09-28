n = int(input())
x = 1
power2 = 0
power5 = 0
for i in range(1, n+1):
    while i%2 == 0:
        i //= 2
        power2 += 1
    while i%5 == 0:
        i //= 5
        power5 += 1
    x *= i
    x %= 1000

power2 -= power5
for _ in range(power2):
    x *= 2
    x %= 1000
s = str(x)
if n > 6 and len(s) < 3:
    s = '0' * (3-len(s)) + s

print(s)
