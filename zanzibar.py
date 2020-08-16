n = int(input())
for i in range(n):
    l = input().split()
    t = 0
    for j in range(len(l)-2):
        t += int(max(0, int(l[j+1])-int(l[j])*2))
    print(t)