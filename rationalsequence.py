t = int(input())
for _ in range(t):
    k, s = input().split()
    p, q = map(int, s.split('/'))
    pos = 0
    i = 0
    while p > 1 or q > 1:
        if p < q:
            q -= p
        else:
            p -= q
            pos += 2**i
        i += 1

    pos += 1
    if pos == 2**i:
        pos = 0
        i += 1

    p, q = 1, 1
    while i > 0:
        i -= 1
        if pos < 2**i:
            q += p
        else:
            p += q
        pos %= 2**i

    print(k, str(p) + '/' + str(q))
