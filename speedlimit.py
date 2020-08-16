while True:
    n = int(input())
    if n > -1:
        prev = 0
        dist = 0
        for i in range(n):
            l = input().split()
            v = int(l[0])
            t = int(l[1])
            dist += v*(t-prev)
            prev = t
        print(str(dist) + " miles")
    else:
        break