c = int(input())
for case in range(1, c+1):
    n, t = map(int, input().split())
    t -= 1
    capacity = [0 for i in range(n)]
    employees = [0 for i in range(n)]
    cars =[[] for i in range(n)]

    e = int(input())
    for __ in range(e):
        h, p = map(int, input().split())
        h -= 1
        if h == t:
            continue
        capacity[h] += p
        employees[h] += 1
        cars[h].append(p)

    possible = True
    ans = ['0' for i in range(n)]
    for h in range(n):
        count = 0
        if employees[h] > capacity[h]:
            possible = False
            break

        cars[h].sort(reverse = True)
        for cap in cars[h]:
            if employees[h] <= 0:
                break
            employees[h] -= cap
            count += 1

        ans[h] = str(count)

    if not possible:
        print(f'Case #{case}: IMPOSSIBLE')
    else:
        print(f'Case #{case}:', ' '.join(ans))
