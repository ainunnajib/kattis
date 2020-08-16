l = input().split()
n = int(l[0])
t = int(l[1])
l = input().split()
for i in range(n):
    x = int(l[i])
    t -= x
    if t < 0:
        print(i)
        quit()
print(n)