n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    k = s[0]
    s = s[1:]

    d = s[1] - s[0]
    arithmetic = True
    for i in range(2, k):
        if s[i] - s[i-1] != d:
            arithmetic = False
            break
    if arithmetic:
        print('arithmetic')
        continue

    s.sort()
    d = s[1] - s[0]
    arithmetic = True
    for i in range(2, k):
        if s[i] - s[i-1] != d:
            arithmetic = False
            break
    if arithmetic:
        print('permuted arithmetic')
    else:
        print('non-arithmetic')
