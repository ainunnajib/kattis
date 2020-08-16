s = input()
a = [ int(x) for x in s.split() ]
while s != '1 2 3 4 5':
    for i in range(4):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            r = ''
            for x in a:
                if r != '':
                    r += ' '
                r += str(x)
            print(r)
            if r == '1 2 3 4 5':
                quit()
    s = r