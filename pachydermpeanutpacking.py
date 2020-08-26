while True:
    n = int(input())
    if n == 0:
        break
    boxes = []
    boxsizes = []
    for _ in range(n):
        s = input().split()
        boxes.append([( float(s[0]), float(s[1]) ), ( float(s[2]), float(s[3]) )])
        boxsizes.append(s[4])
    m = int(input())
    for _ in range(m):
        s = input().split()
        x = float(s[0])
        y = float(s[1])
        b = s[2]
        floor = True
        for i in range(n):
            box = boxes[i]
            if x >= box[0][0] and x <= box[1][0] and y >= box[0][1] and y <= box[1][1]:
                if b == boxsizes[i]:
                    print(b, 'correct')
                else:
                    print(b, boxsizes[i])
                floor = False
                break
        if floor:
            print(b, 'floor')
    print()
