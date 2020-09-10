b, d, c, l = map(int, input().split())
m = l // min(b, d, c)
printed = False
for p in range(m+1):
    for q in range(m+1):
        for r in range(m+1):
            if b*p + d*q + c*r == l:
                print(p, q, r)
                printed = True
if not printed:
    print('impossible')
