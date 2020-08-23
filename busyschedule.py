n = int(input())
while n > 0:
    schedule = []
    for _ in range(n):
        s = input().split()
        h = int(s[0].split(':')[0])
        m = int(s[0].split(':')[1])
        ampm = s[1]
        if h == 12:
            h = 0
        t = h*60 + m + (12*60 if ampm == 'p.m.' else 0)
        schedule.append(t)
    schedule.sort()
    for t in schedule:
        if t >= 12*60:
            ampm = 'p.m.'
            t -= 12*60
        else:
            ampm = 'a.m.'
        h = t // 60
        if h == 0:
            h = 12
        m = t % 60
        mm = ('0' if m < 10 else '') + str(m)
        print(str(h) + ':' + mm, ampm)
    print()
    n = int(input())
