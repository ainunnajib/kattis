s = input()
while s != '0 0 0 0':
    s = s.split()
    d = [ int(x) for x in s ]
    x = d[0]
    for i in range(4):
        d[i] = int((d[i]+40-x)%40)
    for i in range(4):
        d[i] *= 9
    first = (360 - d[1])%360
    second = (360 + d[2] - d[1])%360
    third = (360 + d[2] - d[3])%360
    result = int(360*3 + first + second + third)
    print(result)
    s = input()