s = input()
while s != '0 0':
    s = s.split()
    x = s[0][::-1]
    y = s[1][::-1]
    c = 0
    carries = 0
    for i in range(min(len(x), len(y))):
        if int(x[i]) + int(y[i]) + c > 9:
            c = 1
            carries += 1
        else:
            c = 0
    if len(x) > len(y):
        for i in range(len(y), len(x)):
            if int(x[i]) + c > 9:
                c = 1
                carries += 1
            else:
                c = 0
    elif len(y) > len(x):
        for i in range(len(x), len(y)):
            if int(y[i]) + c > 9:
                c = 1
                carries += 1
            else:
                c = 0
    if carries == 0:
        print('No carry operation.')
    elif carries == 1:
        print('1 carry operation.')
    else:
        print(f'{carries} carry operations.')

    s = input()
