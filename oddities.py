n = int(input())
for i in range(n):
    k = int(input())
    if int(k/2)*2 == k:
        print(str(k) + " is even")
    else:
        print(str(k) + " is odd")
    