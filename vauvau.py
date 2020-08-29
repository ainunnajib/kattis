a, b, c, d = map(int, input().split())
v = list(map(int, input().split()))
for i in v:
    i -= 1
    x = i%(a+b) < a
    y = i%(c+d) < c
    if x and y:
        print('both')
    elif x or y:
        print('one')
    else:
        print('none')
