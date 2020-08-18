h, w, n = map(int, input().split())
b = list(map(int, input().split()))
x = 0
y = 0
possible = True
i = 0
while i < n:
    while x < w:
        x += b[i]
        i += 1
    if x > w:
        possible = False
        break
    else:
        x = 0
        y += 1
    if y == h:
        possible = True
        break
print("YES" if possible else "NO")
