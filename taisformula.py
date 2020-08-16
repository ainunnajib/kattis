n = int(input())
l = input().split()
prevt = int(l[0])
prevg = float(l[1])
total = 0.0
for i in range(1,n):
    l = input().split()
    t = int(l[0])
    g = float(l[1])
    total += (t-prevt)/1000.0*(g+prevg)/2.0
    prevt = t
    prevg = g
print(total)