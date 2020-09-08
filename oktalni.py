s = input()
n = 0
x = 1
for i in s[::-1]:
    n += int(i) * x
    x *= 2
r = ''
while n > 0:
    r = str(n%8) + r
    n //= 8
print(r)
