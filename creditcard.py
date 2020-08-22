n = int(input())
for _ in range(n):
    a = input().split()
    r, b, m = 0, 0, 0
    x = a[0].split('.')
    r = 100*int(x[0]) + int(x[1])
    x = a[1].split('.')
    b = 100*int(x[0]) + int(x[1])
    x = a[2].split('.')
    m = 100*int(x[0]) + int(x[1])

    for i in range(1, 1201):
        interest = (r*b*2+10000)//20000
        b += interest
        b -= m
        if b <= 0:
            print(i)
            break
    if i == 1200 and b > 0:
        print("impossible")
