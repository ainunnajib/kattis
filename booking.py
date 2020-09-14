from datetime import datetime, timedelta
t = int(raw_input())
for _ in range(t):
    b, c = map(int, raw_input().split())
    l = []
    for __ in range(b):
        code, fromd, fromt, tod, tot = raw_input().split()
        fd = datetime.strptime(fromd + ' ' + fromt, '%Y-%m-%d %H:%M')
        td = datetime.strptime(tod + ' ' + tot, '%Y-%m-%d %H:%M')
        ct = timedelta(minutes = c)
        td += ct
        l.append((fd, 1))
        l.append((td, -1))
    l.sort()
    maxroom = 0
    curroom = 0
    for r in l:
        curroom += r[1]
        maxroom = max(maxroom, curroom)
    print(maxroom)
