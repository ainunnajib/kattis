n = int(input())
q = list(input())
m, count = 0, 0
printed = False
while len(q) > 0:
    if q[0] == 'M':
        if abs(m+1) > n:
            if q[1] == 'W':
                q.pop(1)
                m -= 1
                count += 1
            else:
                print(count)
                printed = True
                break
        else:
            q.pop(0)
            m += 1
            count += 1
    else:
        if abs(m-1) > n:
            if q[1] == 'M':
                q.pop(1)
                m += 1
                count += 1
            else:
                print(count)
                printed = True
                break
        else:
            q.pop(0)
            m -= 1
            count += 1
if not printed:
    print(count)
