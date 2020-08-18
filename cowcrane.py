m, l = map(int, input().split())
M, L = map(int, input().split())
tm, tl = map(int, input().split())
t = 0

# m then l
possible = True
t = abs(m) + abs(m-M)
if t > tm:
    possible = False
else:
    t += abs(M-l) + abs(L-l)
    if t > tl:
        possible = False
if possible:
    print("possible")
else:
    # l then m
    possible = True
    t = abs(l) + abs(l-L)
    if t > tl:
        possible = False
    else:
        t += abs(L-m) + abs(M-m)
        if t > tm:
            possible = False
    if possible:
        print("possible")
    else:
        # m to l, then l, then m
        possible = True
        t = abs(m) + abs(l-m) + abs(L-l)
        if t > tl:
            possible = False
        else:
            t += abs(L-l) + abs(M-l)
            if t > tm:
                possible = False
        if possible:
            print("possible")
        else:
            # l to m, then m, then l
            possible = True
            t = abs(l) + abs(l-m) + abs(M-m)
            if t > tm:
                possible = False
            else:
                t += abs(M-m) + abs(L-m)
                if t > tl:
                    possible = False
            if possible:
                print("possible")
            else:
                print("impossible")
