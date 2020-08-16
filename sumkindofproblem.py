n = int(input())
for i in range(n):
    l = input().split()
    x = l[0]
    k = int(l[1])
    a = int(k*(k+1)/2)
    b = k*k
    c = k*(k+1)
    print(x+' '+str(a)+' '+str(b)+' '+str(c))