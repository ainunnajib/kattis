d = {'UTC':0, 'GMT':0, 'WET':0,
     'BST':1, 'IST':1, 'WEST':1, 'CET':1,
     'CEST':2, 'EET':2,
     'EEST':3, 'MSK':3,
     'MSD':4,
     'AWST':8,
     'ACST':9.5,
     'AEST':10,
     'ACDT':10.5,
     'AEDT':11,
     'HST':-10,
     'AKST':-9,
     'PST':-8, 'AKDT':-8,
     'MST':-7, 'PDT':-7,
     'CST':-6, 'MDT':-6,
     'EST':-5, 'CDT':-5,
     'AST':-4, 'EDT':-4,
     'NST':-3.5,
     'ADT':-3,
     'NDT':-2.5
    }
n = int(input())
for _ in range(n):
    s = input().split()
    t = 0
    if s[0] in ['noon', 'midnight']:
        fromtz = d[s[1]]
        totz = d[s[2]]
        if s[0] == 'noon':
            t = 12*60
    else:
        fromtz = d[s[2]]
        totz = d[s[3]]
        hour = int(s[0].split(':')[0])
        minute = int(s[0].split(':')[1])
        if hour == 12 and s[1] == 'a.m.':
            hour = 0
        t = hour*60+minute
        if s[1] == 'p.m.' and hour < 12:
            t += 12*60
    t += (totz-fromtz)*60
    t %= 24*60
    if t == 0:
        print('midnight')
    elif t == 12*60:
        print('noon')
    else:
        hour = int((t // 60) % 12)
        if hour == 0:
            hour = 12
        minute = int(t % 60)
        if t > 12*60:
            ampm = 'p.m.'
        else:
            ampm = 'a.m.'
        print(str(hour)+':'+('0' if minute < 10 else '')+str(minute), ampm)
