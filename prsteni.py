def gcd(x, y):
    if x < y:
        x = x+y
        y = x-y
        x = x-y
    if y == 0:
        return x
    elif y == 1:
        return 1
    else:
        return gcd(y, x-y)

n = int(input())
s = input().split()
a = [ int(x) for x in s]
base = a[0]
for i in range(1,n):
    p = gcd(base, a[i])
    print(str(int(base/p))+'/'+str(int(a[i]/p)))