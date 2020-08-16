n = int(input())
s = ""
a = []
for i in range(n):
    name = input()
    s += name
    a.append(name)
a.sort()
x = ''.join(a)
if s == x:
    print("INCREASING")
else:
    a.reverse()
    x = ''.join(a)
    if s == x:
        print("DECREASING")
    else:
        print("NEITHER")