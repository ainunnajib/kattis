t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    i = 0
    count = 0
    for x in l:
        if x == i + 1:
            i += 1
        else:
            count += 1

    print(count)
