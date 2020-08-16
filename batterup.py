denum = int(input())
l = input().split()
num = 0
for c in l:
    if int(c) < 0:
        denum -= 1
    else:
        num += int(c)
print(1.0*num/denum)