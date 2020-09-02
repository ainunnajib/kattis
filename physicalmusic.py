import sys
inputs = iter(sys.stdin.readlines())
t = int(next(inputs))
for _ in range(t):
    n = int(next(inputs))
    all = [0 for i in range(n+1)]
    cd = []
    for i in range(1, n+1):
        x = int(next(inputs))
        if all[x] < x-1:
            cd.append(x)
        for j in range(x, n+1):
            all[j] += 1
    print(len(cd))
    cd.sort()
    for x in cd:
        print(x)
