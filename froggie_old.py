l, w = map(int, input().split())
lanes = [[True for x in range(w)] for y in range(l+2)]
cars = [[] for y in range(l+2)]
safe = True
for y in range(l, 0, -1):
    o, i, s = map(int, input().split())
    cars[y] = [o, i, s]
inp = input().split()
m = int(inp[0]) # m, n will be position of froggie
n = 0
steps = inp[1]

for step in steps:
    # update the states of lanes, 0 to w-1 based on direction
    for q in range(len(lanes)):
        for p in range(w):
            lanes[q][p] = True

    for y in range(l, 0, -1):
        o, i, s = cars[y][0], cars[y][1], cars[y][2]
        for x in range(w):
            if (x-o-1)%i < s or (s == 0 and (x-o)%i == 0):
                lanes[y][x] = False
        o += s
        o %= i
        cars[y][0] = o

    # froggie makes the step
    against = False
    b = n
    prevb = b
    if step == 'U':
        b += 1
    elif step == 'D':
        b -= 1

    if (l-b+1)%2 == 1: #odd lane, keep the same coordinate
        a = m
        preva = a
        if step == 'L':
            a -= 1
            against = True
        elif step == 'R':
            a += 1
            against = False
    else: #even lane, reverse direction
        a = (w-1-m)%w
        preva = a
        if step == 'L':
            a += 1
            against = False
        elif step == 'R':
            a -= 1
            against = True

    #print(m, n, step, a, b, lanes[b][a])
    for q in range(len(lanes)-1, -1, -1):
        row = ""
        for p in lanes[q]:
            if (l-q+1)%2 == 1:
                row += ('-' if p else '#')
            else:
                row = ('-' if p else '#') + row
        #print(row)

    if not lanes[b][a] or (step in ['L', 'R'] and against and not lanes[prevb][preva]):
        safe = False

    if (l-b+1)%2 == 1: #odd lane, keep the same coordinate
        m = a
        n = b
    else:
        m = (w-1-a)%w
        n = b

    if n == l+1:
        break

if safe and n == l+1:
    print('safe')
else:
    print('squish')
