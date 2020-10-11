from collections import defaultdict

t = int(input())
for _ in range(t):
    input()
    n = int(input())
    l = list(map(int, input().split()))

    cumsum = defaultdict(int)
    cumsum[0] = 1
    sumsofar = 0
    count = 0

    for x in l:
        sumsofar += x
        count += cumsum[sumsofar-47]
        cumsum[sumsofar] += 1

    print(count)
