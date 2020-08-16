n = int(input())
l = input().split()
bus = [ int(x) for x in l ]
bus.sort()
r = str(bus[0])
start = bus[0]
for i in range(1,n):
    if bus[i] > bus[i-1]+1:
        r += (" "+str(bus[i]))
        start = bus[i]
    elif i == n-1 or bus[i+1] > bus[i]+1:
        if start == bus[i] - 1:
            r += (" "+str(bus[i]))
            start = bus[i]
        else:
            r += ("-"+str(bus[i]))
            if i < n-1:
                start = bus[i]+1
print(r)