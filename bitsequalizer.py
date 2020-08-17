c = int(input())
for j in range(c):
    a = input()
    b = input()
    l = len(a)
    w0, w1, vs0, vs1 = 0, 0, 0, 0
    for i in range(l):
        if a[i] != b[i]:
            if a[i] == '0':
                w0 += 1
            elif a[i] == '1':
                w1 += 1
            elif a[i] == '?':
                if b[i] == '0':
                    vs0 += 1
                elif b[i] == '1':
                    vs1 += 1
    # swap matching misplaced (0,1)s
    answer = min(w0, w1)
    w0 -= answer
    w1 -= answer
    # still misplaced 1s left
    if w0 == 0:
        if w1 > vs1: # not enough wildcard vs1 to swap with
            answer = -1
        else: # make vs1 become 0 and swap
            vs1 -= w1
            answer += 2*w1 + vs1 + vs0
    else:
        answer += w0 + vs1 + vs0
    print("Case " + str(j+1) + ": " + str(answer))
