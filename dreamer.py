from itertools import permutations
from datetime import datetime

t = int(raw_input())
for _ in range(t):
    s = list(raw_input().replace(' ', ''))
    count = 0
    mindate = None
    dates = set()
    for l in permutations(s):
        dd = int(''.join(l[:2]))
        mm = int(''.join(l[2:4]))
        yyyy = int(''.join(l[4:]))

        if yyyy < 2000:
            continue

        try:
            d = datetime(yyyy, mm, dd)
        except Exception as e:
            continue

        if d not in dates:
            count += 1
            dates.add(d)

        if mindate == None or mindate > d:
            mindate = d

    if mindate == None:
        print(0)
    else:
        dd = str(mindate.day).zfill(2)
        mm = str(mindate.month).zfill(2)
        print(str(count) + ' ' + dd + ' ' + mm + ' ' + str(mindate.year))
