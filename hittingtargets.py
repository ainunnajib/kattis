rectangles = []
circles = []
m = int(input())
for _ in range(m):
    s = input().split()
    if s[0] == 'rectangle':
        x1, y1, x2, y2 = map(int, s[1:])
        rectangles.append((x1, y1, x2, y2))
    else:
        x, y, r = map(int, s[1:])
        circles.append((x, y, r))
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    hit = 0
    for r in rectangles:
        if x >= r[0] and y >= r[1] and x <= r[2] and y <= r[3]:
            hit += 1
    for c in circles:
        if (x - c[0])**2 + (y - c[1])**2 <= c[2]**2:
            hit += 1
    print(hit)
