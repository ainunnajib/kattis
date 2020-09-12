k = int(input())
n = k
i = 0
while n%2 == 0:
    n = n >> 1
    i += 1
if n == 1:
    print(1 << i, 0)
else:
    j = i
    while n > 0:
        n = n >> 1
        j += 1
    print(1 << j, j-i)
