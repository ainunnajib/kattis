n = int(input())
r = 'ABCDEFGH'
for _ in range(n):
    s = input().split()
    a = r.index(s[0])
    b = int(s[1])-1
    x = r.index(s[2])
    y = int(s[3])-1
    m = abs(x-a)
    n = abs(y-b)
    if a == x and b == y:
        print(0,s[0],s[1])
    elif m == n:
        print(1, s[0],s[1], s[2],s[3])
    elif (m+n)%2 != 0:
        print("Impossible")
    else:
        if m > n:
            # move horizontally
            extra = (m-n)//2
            extraplus = extra + n
            if x > a: # move to right
                if max(b,y)+extra < 8:
                    # up first
                    if y <= b:
                        print(2, s[0],s[1], r[a+extra],(max(b,y)+extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[a+extraplus],(max(b,y)+extra+1), s[2],s[3])
                elif min(b,y)-extra >= 0:
                    # down first
                    if y >= b:
                        print(2, s[0],s[1], r[a+extra],(min(b,y)-extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[a+extraplus],(min(b,y)-extra+1), s[2],s[3])
            elif x < a: # move to left
                if max(b,y)+extra < 8:
                    # up first
                    if y <= b:
                        print(2, s[0],s[1], r[a-extra],(max(b,y)+extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[a-extraplus],(max(b,y)+extra+1), s[2],s[3])
                elif min(b,y)-extra >= 0:
                    # down first
                    if y >= b:
                        print(2, s[0],s[1], r[a-extra],(min(b,y)-extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[a-extraplus],(min(b,y)-extra+1), s[2],s[3])
        elif m < n:
            # move vertically
            extra = (n-m)//2
            extraplus = extra + m
            if y > b: # move up
                if max(a,x)+extra < 8:
                    # right first
                    if x <= a:
                        print(2, s[0],s[1], r[max(a,x)+extra],(b+extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[max(a,x)+extra],(b+extraplus+1), s[2],s[3])
                elif min(a,x)-extra >= 0:
                    # left first
                    if x >= a:
                        print(2, s[0],s[1], r[min(a,x)-extra],(b+extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[min(a,x)-extra],(b+extraplus+1), s[2],s[3])
            elif y < b: # move down
                if max(a,x)+extra < 8:
                    # right first
                    if x <= a:
                        print(2, s[0],s[1], r[max(a,x)+extra],(b-extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[max(a,x)+extra],(b-extraplus+1), s[2],s[3])
                elif min(a,x)-extra >= 0:
                    # left first
                    if x >= a:
                        print(2, s[0],s[1], r[min(a,x)-extra],(b-extra+1), s[2],s[3])
                    else:
                        print(2, s[0],s[1], r[min(a,x)-extra],(b-extraplus+1), s[2],s[3])
