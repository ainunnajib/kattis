l = input().split()
while l[0] != "0" or l[1] != "0":
    x = int(l[0])
    y = int(l[1])
    a = int(x/y)
    b = x%y
    print(str(a) + " " + str(b) + " / " + str(y))
    l = input().split()
    