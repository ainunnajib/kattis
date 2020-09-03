n = int(input())
while n != 0:
    n -= 1
    bits = []
    while n > 0:
        bits.append(n%2 == 1)
        n //= 2
    powers = []
    p = 1
    for b in bits:
        if b:
            powers.append(p)
        p *= 3
    ps = [str(p) for p in powers]
    if ps == []:
        print('{ }')
    else:
        print('{', ', '.join(ps) ,'}')
    n = int(input())
