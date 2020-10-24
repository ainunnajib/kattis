t = int(input())
l = []
for _ in range(t):
    l.append(int(input()))

for a in range(10001):
    for b in range(10001):
        s = []
        valid = True
        for i in range(t-1):
            x = l[i]
            x = (a*x + b) % 10001
            s.append(x)
            x = (a*x + b) % 10001
            if l[i+1] != x:
                valid = False
                break
        if valid:
            x = (a*x + b) % 10001
            s.append(x)
            for x in s:
                print(x)
            break
    if valid:
        break
