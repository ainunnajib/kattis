from collections import defaultdict

n = int(input())
while n > -1:
    if n < 10:
        print(10+n)
    else:
        f = defaultdict(int)
        for p in [2, 3, 5, 7]:
            while n % p == 0:
                n //= p
                f[p] += 1
        if n > 1:
            print('There is no such number.')
        else:
            s = ''
            while f[3] >= 2:
                s += '9'
                f[3] -= 2

            while f[2] >= 3:
                s = '8' + s
                f[2] -= 3

            s = '7' * f[7] + s

            if f[2] > 0 and f[3] > 0:
                s = '6' + s
                f[2] -= 1
                f[3] -= 1

            s = '5' * f[5] + s

            if f[2] == 2:
                s = '4' + s
                f[2] -= 2

            if f[3] > 0:
                s = '3' + s

            if f[2] > 0:
                s = '2' + s

            print(s)
    
    n = int(input())
