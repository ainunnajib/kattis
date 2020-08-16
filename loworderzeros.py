a = [ 1 for x in range(1000001)]
r = 1
for i in range(1, 1000001):
    r = r * i
    while r%10 == 0:
        r = int(r/10)
    r = r%100000000
    a[i] = r%10

n = int(input())
while n > 0:
    print(a[n])
    n = int(input())