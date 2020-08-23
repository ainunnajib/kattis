while True:
    try:
        s = input().split()
        starthour, startminute = map(int, s[3].split(':'))
        endhour, endminute = map(int, s[4].split(':'))
        duration = (endhour - starthour) * 60 + (endminute - startminute)
        durationhour = int(duration // 60)
        durationminute = int(duration % 60)
        print(s[0], s[1], s[2], durationhour, 'hours', durationminute, 'minutes')
    except EOFError:
        break
