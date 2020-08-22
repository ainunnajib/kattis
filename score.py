score = {'H':0, 'A':0}
leadtime = {'H':0, 'A':0, 'draw':0}
lasttime = 0
leader = 'draw'
n = int(input())
for _ in range(n):
    a = input().split()
    m, s = map(int, a[2].split(':'))
    t = 60*m+s
    leadtime[leader] += t - lasttime
    lasttime = t
    score[a[0]] += int(a[1])
    if score['H'] == score['A']:
        leader = 'draw'
    elif score['H'] > score['A']:
        leader = 'H'
    else:
        leader = 'A'
leadtime[leader] += 32*60 - lasttime
m = leadtime['H']//60
s = leadtime['H']%60
h = str(m) + ':' + ('' if s > 9 else '0') + str(s)
m = leadtime['A']//60
s = leadtime['A']%60
a = str(m) + ':' + ('' if s > 9 else '0') + str(s)
print(leader, h, a)
