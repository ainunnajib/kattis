x, ans = 0, 0
for c in input():
    if c.isupper():
        ans += (4-x)%4
        x = 0
    x += 1
    x %= 4
print(ans)