import math
t = int(input())
for _ in range(t):
    k, s = input().split()
    p, q = map(int, s.split('/'))

    if q == 1:
        print(k, '1/'+str(p+1))
    else:
        step = 0
        if p > q:
            step = math.ceil((p-q)/q)
            p -= q * step
        q = q-p
        p = q+p
        if step > 0:
            q += p * step
        print(k, str(p)+'/'+str(q))
