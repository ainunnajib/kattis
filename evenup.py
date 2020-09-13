input()
s = list(map(int, input().split()))
l = []
for x in s:
    if len(l) == 0:
        l.append(x)
    else:
        if (l[-1] + x) % 2 == 0:
            l.pop()
        else:
            l.append(x)
print(len(l))
