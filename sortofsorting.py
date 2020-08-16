n = int(input())
while n > 0:
    names = []
    na = []
    for i in range(n):
        s = input()
        names.append(s)
        na.append(s[:2])
    na.sort()
    prev = ""
    for nn in na:
        if nn != prev:
            prev = nn
            for name in names:
                if name[:2] == nn:
                    print(name)
    print("")
    n = int(input())