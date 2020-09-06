valid = True
n, m = map(int, input().split())
b = []
for _ in range(n):
    b.append(list(input()))

s = [[{'right':False, 'bottom':False} for j in range(m)] for i in range(n)]

def processcell(y, x):
    global valid
    top, left = False, False

    if y > 0:
        top = s[y-1][x]['bottom']
    if x > 0:
        left = s[y][x-1]['right']

    if b[y][x] == 'A':
        if y > 0:
            if top:
                valid = False
        if x > 0:
            if left:
                valid = False

    elif b[y][x] == 'B':
        if y == 0 and x == 0:
            valid = False
        elif y == 0:
            setcheckright(y, x)
        else:
            if top and not left:
                setcheckbottom(y, x)
            elif not top and left:
                setcheckright(y, x)
            else:
                valid = False

    elif b[y][x] == 'C':
        if y == 0 and x == 0:
            setcheckright(y, x)
            setcheckbottom(y, x)
        elif y == 0:
            setcheckbottom(y, x)
            if not left:
                setcheckright(y, x)
        else:
            if top:
                if not left:
                    setcheckright(y, x)
            else:
                setcheckbottom(y, x)
                if not left:
                    setcheckright(y, x)

    elif b[y][x] == 'D':
        if y == 0 or x == 0 or y == n-1 or x == m-1:
            valid = False
        else:
            if not top:
                valid = False
            if not left:
                valid = False
            setcheckright(y, x)
            setcheckbottom(y, x)

def setcheckbottom(y, x):
    global valid
    s[y][x]['bottom'] = True
    if y == n-1:
        valid = False

def setcheckright(y, x):
    global valid
    s[y][x]['right'] = True
    if x == m-1:
        valid = False

for k in range(min(n, m)):
    # row first
    for i in range(k, m):
        processcell(k, i)
    # then column
    for j in range(k, n):
        processcell(j, k)

    if not valid:
        break

if valid:
    print('Possible')
else:
    print('Impossible')
