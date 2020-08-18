a, b, h = map(int, input().split())
steps = 0
while h > 0:
    h -= a
    steps += 1
    if h <= 0:
        break
    h += b
print(steps)
