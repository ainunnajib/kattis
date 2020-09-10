x1, x2 = map(int, input().split())
t1 = [-1 for i in range(3000001)]
t2 = [-1 for i in range(3000001)]

t = list(map(int, input().split()))
lt = t[0]
t = t[1:]
cx = x1
ct = 0
for i in range(lt//2):
    start = t[2*i]
    end = t[2*i+1]
    for at in range(ct, start):
        t1[at] = cx
    for at in range(start, end):
        cx += 1
        t1[at] = cx
    ct = end
if lt%2 == 1:
    start = t[-1]
    for at in range(ct, start):
        t1[at] = cx
    for at in range(start, 3000001):
        cx += 1
        t1[at] = cx
else:
    for at in range(ct, 3000001):
        t1[at] = cx

t = list(map(int, input().split()))
lt = t[0]
t = t[1:]
cx = x2
ct = 0
for i in range(lt//2):
    start = t[2*i]
    end = t[2*i+1]
    for at in range(ct, start):
        t2[at] = cx
    for at in range(start, end):
        cx += 1
        t2[at] = cx
    ct = end
if lt%2 == 1:
    start = t[-1]
    for at in range(ct, start):
        t2[at] = cx
    for at in range(start, 3000001):
        cx += 1
        t2[at] = cx
else:
    for at in range(ct, 3000001):
        t2[at] = cx

safe = True
if x1 > x2:
    for t in range(3000001):
        if t1[t] < t2[t] + 4.4:
            print(f'bumper tap at time {t+1}')
            safe = False
            break
    if safe:
        print('safe and sound')
else:
    for t in range(3000001):
        if t2[t] < t1[t] + 4.4:
            print(f'bumper tap at time {t+1}')
            safe = False
            break
    if safe:
        print('safe and sound')
