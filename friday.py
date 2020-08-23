t = int(input())
for _ in range(t):
    d, m = map(int, input().split())
    months = list(map(int, input().split()))
    count = 0
    startday = 1
    for month in months:
        if month >= 13 and (startday + 12) % 7 == 6:
            count += 1
        startday = (startday + month) % 7
    print(count)
