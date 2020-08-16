start = int(input())
n = int(input())
t = 0
for i in range(n):
    l = input().split()
    t += int(l[0])
    if t >= 210:
        print(start)
        break
    if l[1] == "T":
        start = int(start%8+1)