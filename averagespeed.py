speed = 0
time = 0
dist = 0
while True:
    try:
        l = input().split()
        h, m, s = map(int, l[0].split(':'))
        t = h*3600 + m*60 + s
        dist += (t-time)*speed/3600
        time = t
        if len(l) > 1:
            speed = int(l[1])
        else:
            print(l[0], f'{round(dist, 2):.2f}', 'km')
    except EOFError:
        break
