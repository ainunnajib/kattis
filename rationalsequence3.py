t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    bits = []
    while n > 0:
        bits = [n%2] + bits
        n >>= 1
    p, q = 1, 1
    for x in bits[1:]:
        if x == 0:
            q += p
        else:
            p += q
    print(k, str(p)+'/'+str(q))
