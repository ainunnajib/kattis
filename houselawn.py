lawn, m = map(int, input().split())
l = []
for i in range(m):
    name, p, c, t, r = input().split(',')
    p, c, t, r = map(int, (p, c, t, r))

    mowtime = (10080 // (t + r)) * t + min(10080 % (t + r), t)
    if lawn <= mowtime * c and c * t * 10080 >= lawn * (t + r):
        l.append((p, i, name))

if len(l) == 0:
    print('no such mower')
else:
    l.sort()
    price = l[0][0]
    for p, i, name in l:
        if p == price:
            print(name)
        else:
            break
