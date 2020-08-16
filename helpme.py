white = []
black = []
c = 'abcdefgh'
r = '87654321'
for i in range(17):
    s = input()
    if i%2 == 1:
        row = r[int((i-1)/2)]
        for j in range(33):
            if j%4 == 2:
                col = c[int((j-2)/4)]
                if s[j] in 'KQRBN':
                    white.append(s[j]+col+row)
                elif s[j] == 'P':
                    white.append(col+row)
                elif s[j] in 'kqrbn':
                    black.append(s[j].upper()+col+row)
                elif s[j] == 'p':
                    black.append(col+row)
result = 'White: '
comma = ''
pieces = []
for piece in white:
    if piece[0] == 'K':
        pieces.append(piece)
pieces.sort()
for row in r[::-1]:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in white:
    if piece[0] == 'Q':
        pieces.append(piece)
pieces.sort()
for row in r[::-1]:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in white:
    if piece[0] == 'R':
        pieces.append(piece)
pieces.sort()
for row in r[::-1]:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in white:
    if piece[0] == 'B':
        pieces.append(piece)
pieces.sort()
for row in r[::-1]:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in white:
    if piece[0] == 'N':
        pieces.append(piece)
pieces.sort()
for row in r[::-1]:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in white:
    if piece[0] not in 'KQRBN':
        pieces.append(piece)
pieces.sort()
for row in r[::-1]:
    for p in pieces:
        if p[1] == row:
            result += comma+p
            comma = ','

print(result)

result = 'Black: '
comma = ''
pieces = []
for piece in black:
    if piece[0] == 'K':
        pieces.append(piece)
pieces.sort()
for row in r:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in black:
    if piece[0] == 'Q':
        pieces.append(piece)
pieces.sort()
for row in r:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in black:
    if piece[0] == 'R':
        pieces.append(piece)
pieces.sort()
for row in r:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in black:
    if piece[0] == 'B':
        pieces.append(piece)
pieces.sort()
for row in r:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in black:
    if piece[0] == 'N':
        pieces.append(piece)
pieces.sort()
for row in r:
    for p in pieces:
        if p[2] == row:
            result += comma+p
            comma = ','

pieces = []
for piece in black:
    if piece[0] not in 'KQRBN':
        pieces.append(piece)
pieces.sort()
for row in r:
    for p in pieces:
        if p[1] == row:
            result += comma+p
            comma = ','
print(result)