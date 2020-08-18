s = input().split()
n = int(s[0])
a = [i for i in range(n)]
count = 0
if s[1] == "out":
    h = (len(a)+1)//2
    h1 = a[:h]
    h2 = a[h:]
    x = []
    for i in range(h):
        x.append(h1[i])
        if i < len(h2):
            x.append(h2[i])
    count += 1
    while x != a:
        h1 = x[:h]
        h2 = x[h:]
        x = []
        for i in range(h):
            x.append(h1[i])
            if i < len(h2):
                x.append(h2[i])
        count += 1
elif s[1] == "in":
    h = len(a)//2
    h1 = a[:h]
    h2 = a[h:]
    x = []
    for i in range(len(h2)):
        x.append(h2[i])
        if i < len(h1):
            x.append(h1[i])
    count += 1
    while x != a:
        h1 = x[:h]
        h2 = x[h:]
        x = []
        for i in range(len(h2)):
            x.append(h2[i])
            if i < len(h1):
                x.append(h1[i])
        count += 1
print(count)
