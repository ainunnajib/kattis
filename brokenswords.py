n = int(input())
x = 0
y = 0
for i in range(n):
    s = input()
    for c in s[:2]:
        if c == '0':
            x += 1
    for c in s[2:4]:
        if c == '0':
            y += 1
swords = min(round(x/2), round(y/2))
x -= 2*swords
y -= 2*swords
print(swords, x, y)
