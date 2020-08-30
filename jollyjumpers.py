while True:
    try:
        s = list(map(int, input().split()))
        n = s[0]
        s = s[1:]
        notincluded = [True for i in range(n)]
        notincluded[0] = False
        for i in range(n-1):
            diff = int(abs(s[i]-s[i+1]))
            if diff < len(s):
                notincluded[diff] = False
        if sum(notincluded) == 0:
            print('Jolly')
        else:
            print('Not jolly')
    except EOFError:
        break
