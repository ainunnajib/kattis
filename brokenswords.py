n = int(input())
x, y = 0, 0
for i in range(n):
    s = input()
    x += s[:2].count('0')
    y += s[2:4].count('0')
swords = min(int(x/2), int(y/2))
x -= 2*swords
y -= 2*swords
print(swords, x, y)
