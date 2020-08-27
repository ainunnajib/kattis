height, width = map(int, input().split())
# states = array of time x (1 + row + 1) x column
offsets = []
intervals = []
speeds = []
for _ in range(height):
    s = list(map(int, input().split()))
    offsets.append(s[0])
    intervals.append(s[1])
    speeds.append(s[2])
s = input().split()
x = int(s[0])
y = height # going upwards means reducing y
steps = s[1]
squished = False
t = 0
while steps[t] != 'U':
    if steps[t] == 'R':
        x += 1
        if x == width:
            x -= 1
    elif steps[t] == 'L':
        x -= 1
        if x == -1:
            x = 0
    t += 1

for step in steps[t:]:
    if step == 'U':
        y -= 1
        if y < 0:
            break
    elif step == 'D':
        y += 1
        if y >= height:
            y = height - 1
    elif step == 'R':
        x += 1
        if x == width:
            x -= 1
    elif step == 'L':
        x -= 1
        if x == -1:
            x = 0

    o = offsets[y]
    i = intervals[y]
    s = speeds[y]

    if s >= i:
        squished = True

    car = (o + t*s)%i
    if y % 2 == 1: # direction to left
        opposite = 'R'
        frog = width-1-x
    else:
        opposite = 'L'
        frog = x

    if s == 0:
        if (frog-car)%i == 0:
            squished = True
    else:
        if (frog-car)%i == 0 and step == opposite:
            squished = True
        elif (frog-car)%i > 0 and (frog-car)%i <= s:
            squished = True

    if squished or y < 0:
        break
    t += 1

if not squished and y < 0:
    print('safe')
else:
    print('squish')
