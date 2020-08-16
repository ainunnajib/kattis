l = input().split()
r = int(l[0])
c = int(l[1])
zr = int(l[2])
zc = int(l[3])
for i in range(r):
    s = input()
    line = ""
    for j in range(c):
        for y in range(zc):
            line += s[j]
    for x in range(zr):
        print(line)