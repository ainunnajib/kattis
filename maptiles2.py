s = input()
z = len(s)
x = 0
y = 0
for c in s:
    x *= 2
    y *= 2
    if c == '1':
        x += 1
    elif c == '2':
        y += 1
    elif c == '3':
        x += 1
        y += 1
print(z, x, y)
