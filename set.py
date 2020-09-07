import itertools
number = {'1':1, '2':8, '3':64}
shape = {'D':1, 'S':8, 'O':64}
style = {'S':1, 'T':8, 'O':64}
color = {'R':1, 'G':8, 'P':64}
valid = {3, 24, 192, 73}

cards = ['']
for _ in range(4):
    for card in input().split():
        cards.append(card)
printed = False
for trio in itertools.combinations([1,2,3,4,5,6,7,8,9,10,11,12], 3):
    a = cards[trio[0]]
    b = cards[trio[1]]
    c = cards[trio[2]]
    if (number[a[0]] + number[b[0]] + number[c[0]] in valid) and (shape[a[1]] + shape[b[1]] + shape[c[1]] in valid) and (style[a[2]] + style[b[2]] + style[c[2]] in valid) and (color[a[3]] + color[b[3]] + color[c[3]] in valid):
        print(trio[0], trio[1], trio[2])
        printed = True
if not printed:
    print('no sets')
