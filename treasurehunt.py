r, c = map(int, input().split())
m = []
for i in range(r):
    m.append(input())
x = 0
y = 0
for i in range(r*c+1):
    if i == r*c:
        print("Lost")
        break
    if x < 0 or y < 0 or x >= c or y >= r:
        print("Out")
        break
    if m[y][x] == 'T':
        print(i)
        break
    if m[y][x] == 'N':
        y -= 1
    elif m[y][x] == 'S':
        y += 1
    elif m[y][x] == 'W':
        x -= 1
    elif m[y][x] == 'E':
        x += 1
