s = input().split()
n = int(s[0])
a = int(s[1])
b = int(s[2])
csquare = a*a + b*b
for i in range(n):
    x = int(input())
    if (x*x > csquare):
        print("NE")
    else:
        print("DA")