n = int(input())
for _ in range(n):
    a = input().split(',')
    r = 0
    for x in a:
        r *= 60
        if x == '':
            x = '0'
        r += int(x)
    print(r)
