q = int(input())
for _ in range(q):
    x = int(input())
    m = 2*x
    n = x
    c = 1
    while m > 0 or n > 0:
        if m > 0:
            c *= m
            m -= 1
        if n > 0:
            if c%(n*n) == 0:
                c //= (n*n)
                n -= 1
    c //= (x+1)
    print(c)
