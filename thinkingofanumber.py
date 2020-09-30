n = int(input())
while n > 0:
    lower, upper = 0, 0
    divisors = set()
    for _ in range(n):
        s = input().split()
        x = int(s[2])

        if s[0][0] == 'l':
            if upper == 0 or upper > x:
                upper = x
        elif s[0][0] == 'g':
            if lower == 0 or lower < x:
                lower = x
        elif s[0][0] == 'd':
            divisors.add(x)

    if upper == 0:
        print('infinite')
    else:
        ans = []
        for i in range(lower+1, upper):
            modulo = 0
            for d in divisors:
                modulo += i%d
            if modulo == 0:
                ans.append(str(i))

        if len(ans) == 0:
            print('none')
        else:
            print(' '.join(ans))

    n = int(input())
