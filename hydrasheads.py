s = input().split()
h = int(s[0])
t = int(s[1])
while h != 0 and t != 0:
    cutheads = 0
    cuttails = 0
    if t > 1:
        cuttails = int((t-1)/2)
        t = t - cuttails*2
    #tails now either 2 or 1 or 0 only
    h += cuttails
    cutheads = int(h/2)
    h = h - cutheads*2
    #heads now either 1 or 0 only
    if h == 0:
        if t == 0:
            print(cutheads + cuttails)
        elif t == 1:
            cuttails += 3+2
            cutheads += 1
            print(cutheads + cuttails)
        else: #2 tails
            cuttails += 2+2
            cutheads += 1
            print(cutheads + cuttails)
    else: # 1 head
        if t == 0:
            print(-1)
        elif t == 1:
            cuttails += 1+1
            cutheads += 1
            print(cutheads + cuttails)
        else: #2 tails
            cuttails += 1
            cutheads += 1
            print(cutheads + cuttails)
            
    s = input().split()
    h = int(s[0])
    t = int(s[1])