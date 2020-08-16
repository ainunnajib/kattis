while True:
    try:
        l = input().split()
        a = int(l[0])
        b = int(l[1])
        if a>b:
            print(a-b)
        else:
            print(b-a)
    except EOFError:
        break