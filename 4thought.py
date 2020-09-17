d = {}
o = ['+', '-', '*', '//']
for a in o:
    for b in o:
        for c in o:
            s = '4 ' + a + ' 4 ' + b + ' 4 ' + c + ' 4'
            r = str(int(eval(s)))
            s = s = '4 ' + a[0] + ' 4 ' + b[0] + ' 4 ' + c[0] + ' 4 = ' + r
            if r not in d:
                d[r] = s
m = int(input())
for _ in range(m):
    s = input()
    if s in d:
        print(d[s])
    else:
        print('no solution')
