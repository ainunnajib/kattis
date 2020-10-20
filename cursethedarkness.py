m = int(input())
for _ in range(m):
    a, b = map(float, input().split())

    possible = False
    n = int(input())
    for __ in range(n):
        x, y = map(float, input().split())
        if (x-a)**2 + (y-b)**2 <= 64:
            possible = True

    print('light a candle' if possible else 'curse the darkness')
