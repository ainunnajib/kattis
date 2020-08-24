import decimal
while True:
    try:
        s = input().split()
        name = ""
        i = 0
        while s[i].isalpha():
            if i > 0:
                name += ' '
            name += s[i]
            i += 1
        i = -1
        while s[i].isalpha():
            if i < -1:
                name = s[i] + ' ' + name
            else:
                name = s[i]
            i -= 1
        total = 0
        count = 0
        for x in s:
            if not x.isalpha():
                total += decimal.Decimal(x)
                count += 1
        print(round(total/count, 6), name)
    except EOFError:
        break
