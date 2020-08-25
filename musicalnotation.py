d = {}
notes = "GFEDCBAgfedcba"
for c in notes:
    d[c] = 0

n = int(input())
s = input().split()
duration = 0
for x in s:
    if len(x) > 1:
        dur = int(x[1:]) + 1
    else:
        dur = 2
    duration += dur
duration -= 1

notation = {}
for c in notes:
    if c in ['F', 'D', 'B', 'g', 'e', 'a']:
        char = '-'
    else:
        char = ' '
    row = []
    for i in range(duration):
        row.append(char)
    notation[c] = row

i = 0
for x in s:
    if len(x) > 1:
        dur = int(x[1:])
    else:
        dur = 1

    for _ in range(dur):
        notation[x[:1]][i] = '*'
        i += 1

    i += 1

for c in notes:
    print(c+':', ''.join(notation[c]))
