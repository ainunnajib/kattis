n = int(input())
for i in range(n):
    s = input().split()
    t = int(s[0])
    d = int(s[1])
    a = int((t+d)/2)
    b = a-d
    if((t+d)%2 > 0 or b < 0 or a < b):
        print('impossible')
    else:
        print(str(a) + ' ' + str(b))