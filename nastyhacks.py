n = int(input())
for i in range(n):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    r = b - c - a
    if r > 0:
        print("advertise")
    elif r == 0:
        print("does not matter")
    else:
        print("do not advertise")