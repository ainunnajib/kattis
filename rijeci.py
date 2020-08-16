n = int(input())
a = 1
b = 0
for i in range(n):
    x = a
    y = b
    a += (y-x)
    b += x
print(str(a) + " " + str(b))