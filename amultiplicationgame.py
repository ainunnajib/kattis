while True:
    try:
        n = int(input())
        p = 1
        while p * 18 < n:
            p *= 18
        if p * 9 >= n:
            print('Stan wins.')
        else:
            print('Ollie wins.')
    except EOFError:
        break
