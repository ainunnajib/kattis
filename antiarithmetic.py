s = input().split()
while s[0] != '0':
    l = [int(x) for x in s[1:]]
    n = len(l)

    d = {}
    for i in range(1, n-1):
        d[i] = set(l[i+1:])

    valid = True
    for i in range(n-2):
        for j in range(i+1, n-1):
            x = (l[j] - l[i]) + l[j]
            if x in d[j]:
                valid = False
                break

    print('yes' if valid else 'no')

    s = input().split()
