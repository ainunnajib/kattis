while True:
    try:
        s = input()
        b = bin(int.from_bytes(s.encode(), "big"))
        b = b[2:]
        lb = len(b)
        l = lb + (-1*lb)%8
        ones = b.count('1')
        zeros = l - l//8 - ones
        print('trapped' if (ones%2 == 1 or zeros%2 == 1) else 'free')
    except EOFError:
        break
