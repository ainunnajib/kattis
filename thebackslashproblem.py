while True:
    try:
        n = int(input())
        bs = '\\' * (2**n - 1)
        s = input()
        l = []
        for c in s:
            if (c >= '!' and c <= '*') or (c >= '[' and c <= ']'):
                l += bs + c
            else:
                l += c
        print(''.join(l))

    except EOFError:
        break
