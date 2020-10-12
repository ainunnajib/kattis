n, m = map(int, input().split())
while n + m > 0:
    dragons = []
    for _ in range(n):
        dragons.append(int(input()))
    dragons.sort()

    knights = []
    for _ in range(m):
        knights.append(int(input()))
    knights.sort()

    i = 0
    gold = 0
    for k in knights:
        if k >= dragons[i]:
            gold += k
            i += 1
            if i == n:
                break
    if i == n:
        print(gold)
    else:
        print('Loowater is doomed!')

    n, m = map(int, input().split())
