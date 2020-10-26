d, n = input().split()
while d != '0.0' and n != '0':
    d = float(d)
    n = int(n)
    l = []
    for _ in range(n):
        x, y = map(float, input().split())
        l.append((x, y))

    sour = [False for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if (l[i][0]-l[j][0])**2 + (l[i][1]-l[j][1])**2 <= d**2:
                sour[i] = True
                sour[j] = True

    print(f'{sum(sour)} sour, {n - sum(sour)} sweet')

    d, n = input().split()
