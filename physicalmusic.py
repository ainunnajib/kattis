import sys
inputs = iter(sys.stdin.readlines())
t = int(next(inputs))
for _ in range(t):
    n = int(next(inputs))

    rank = []
    for __ in range(n):
        rank.append(int(next(inputs)))

    minsofar = n+1
    cd = []
    for x in rank[::-1]:
        if x > minsofar:
            cd.append(x)
        minsofar = min(minsofar, x)

    print(len(cd))
    cd.sort()
    for x in cd:
        print(x)
