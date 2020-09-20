import math
while True:
    try:
        r, x, y = map(float, input().split())
        l = math.sqrt(x**2 + y**2)
        if l > r:
            print('miss')
        else:
            arcarea = math.acos(l/r) * r**2
            trianglearea = l**2 * math.tan(math.acos(l/r))
            chordarea = arcarea - trianglearea
            biggerarea = math.pi * r**2 - chordarea
            print(biggerarea, chordarea)
    except EOFError:
        break
