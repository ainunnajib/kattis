t = int(input())
for _ in range(t):
    k, s = input().split()
    a, b = map(int, s.split('/'))
    bits = []
    p, q = a, b
    while p > 1 or q > 1:
        if p < q:
            q -= p
            bits.append(0)
        else:
            p -= q
            bits.append(1)
    pos = 2**len(bits)
    for i in range(len(bits)):
        pos += bits[i]*(2**i)
    print(k, pos)
