n = int(input())
for i in range(n):
    l = input().split()
    b = int(l[0])
    p = float(l[1])
    x = round(60.0*(b-1)/p,4)
    y = round(60.0*b/p,4)
    z = round(60.0*(b+1)/p,4)
    print(str(x) + " " + str(y) + " " + str(z))