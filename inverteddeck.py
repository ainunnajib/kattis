n = int(input())
s = list(map(int, input().split()))
r = s[::-1].copy()

a = []
a.append(s[0])
cur = s[0]
for x in s[1:]:
    if x != cur:
        a.append(x)
        cur = x
nn = len(a)
srt = sorted(a).copy()

mina = min(a)
maxa = max(a)
minai = s.index(mina)
maxai = r.index(maxa)

if a == srt:
    print(n//2, n//2)
elif minai == 0 and maxai == 0:
    start = 0
    while True:
        if start + 1 < nn:
            if a[start+1] > a[start]:
                start += 1
            else:
                break
        else:
            break
    end = nn - 1
    while True:
        if end - 1 >= 0:
            if a[end-1] < a[end]:
                end -= 1
            else:
                break
        else:
            break
    if end >= start and (a[:start] + a[start:end+1][::-1] + a[end+1:]) == srt:
        print(s.index(a[start])+1, n - r.index(a[end]))
    else:
        print('impossible')
elif minai == 0:
    start = 0
    while True:
        if start + 1 < nn:
            if a[start+1] > a[start]:
                start += 1
            else:
                break
        else:
            break
    if (a[:start] + a[start:nn][::-1] == srt):
        print(s.index(a[start])+1, n)
    else:
        print('impossible')
elif maxai == 0:
    end = nn - 1
    while True:
        if end - 1 >= 0:
            if a[end-1] < a[end]:
                end -= 1
            else:
                break
        else:
            break
    if (a[:end+1][::-1] + a[end+1:]) == srt:
        print(s.index(1, n - r.index(a[end])))
    else:
        print('impossible')
else:
    print('impossible')
