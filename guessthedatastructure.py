while True:
    try:
        s, q, pq = [], [], []
        isstack, isqueue, ispriorityqueue, possible = True, True, True, True
        n = int(input())
        for _ in range(n):
            c, x = map(int, input().split())
            if c == 1:
                s.append(x)
                q = [x] + q
                pq.append(x)
                pq.sort()
            else:
                if possible and isstack:
                    if len(s) > 0:
                        if s[-1] == x:
                            s.pop()
                        else:
                            isstack = False
                    else:
                        possible = False
                if possible and isqueue:
                    if len(q) > 0:
                        if q[-1] == x:
                            q.pop()
                        else:
                            isqueue = False
                    else:
                        possible = False
                if possible and ispriorityqueue:
                    if len(pq) > 0:
                        if pq[-1] == x:
                            pq.pop()
                        else:
                            ispriorityqueue = False
                    else:
                        possible = False
        if not possible or isstack + isqueue + ispriorityqueue == 0:
            print('impossible')
        elif isstack + isqueue + ispriorityqueue > 1:
            print('not sure')
        elif isstack:
            print('stack')
        elif isqueue:
            print('queue')
        elif ispriorityqueue:
            print('priority queue')
    except EOFError:
        break
