l = input().split()
n = int(l[0]) + int(l[1])
k = int(l[2])
total = 0
while n >= k:
    n -= (k-1)
    total += 1
print(total)