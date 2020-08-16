n = int(input())
while n != 0:
    a = []
    s1 = []
    for i in range(n):
        x = int(input())
        a.append(x)
        s1.append(x)
    s1.sort()
    b = []
    s2 = []
    for i in range(n):
        x = int(input())
        b.append(x)
        s2.append(x)
    s2.sort()
    for z in a:
        print(s2[s1.index(z)])
    print('')
    n = int(input())