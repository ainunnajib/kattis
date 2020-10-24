import math
d = int(input())
done = False
for i in range(1, math.floor(math.sqrt(d))+1):
    if d%i == 0:
        j = d//i
        if i%2 == j%2:
            a = abs(i-j)//2
            b = (i+j)//2
            print(a, b)
            done = True
            break
if not done:
    print('impossible')
