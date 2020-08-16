l = input().split()
x = int(l[0])
y = int(l[1])
n = int(l[2])
for i in range(1,n+1):
    a = ""
    b = ""
    if int(i/x)*x==i:
        a = "Fizz"
    if int(i/y)*y==i:
        b = "Buzz"
    c = a + b
    if c=="":
        print(i)
    else:
        print(c)