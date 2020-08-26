s = input()
while s != '0 0':
    xs = s.split()[0]
    ys = s.split()[1]
    xi = int(xs)
    yi = int(ys)
    ri = xi*yi
    rs = str(ri)
    lx = len(xs)
    ly = len(ys)
    lr = len(rs)

    row = "+"
    for i in range(2+4*lx+1):
        row += '-'
    row += '+'
    print(row)

    row = "|  "
    for i in range(lx):
        row += ' ' + xs[i] + '  '
    row += ' |'
    print(row)

    row = "| +"
    for i in range(lx):
        row += '---+'
    row += ' |'
    print(row)

    for j in range(ly):
        b = ys[j]
        n = int(b)
        #first row in the cell
        row = "|"
        if lr > lx + ly - j:
            row += '/|'
        else:
            row += ' |'
        for a in xs:
            m = int(a)
            mn = m*n
            row += str(mn//10) + ' /|'
        row += ' |'
        print(row)
        #second row in the cell
        row = "| |"
        for a in xs:
            row += ' / |'
        row += b + '|'
        print(row)
        #third row in the cell
        row = "|"
        if lr >= lx + ly - j:
            row += rs[lr-lx-ly+j] + '|'
        else:
            row += ' |'
        for a in xs:
            m = int(a)
            mn = m*n
            row += '/ ' + str(mn%10) + '|'
        row += ' |'
        print(row)
        #floor the cell
        row = "| +"
        for i in range(lx):
            row += '---+'
        row += ' |'
        print(row)

    row = "|"
    if lr > lx:
        row += '/ '
    else:
        row += '  '
    for i in range(lx):
        row += rs[lr-lx+i]
        if i < lx-1:
            row += ' / '
    row += '    |'
    print(row)

    row = "+"
    for i in range(2+4*lx+1):
        row += '-'
    row += '+'
    print(row)

    s = input()
