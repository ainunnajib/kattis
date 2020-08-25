s = input()
n = len(s)//3
a = s[:n]
b = s[n:2*n]
c = s[2*n:3*n]
if a == b or a == c:
    print(a)
elif b == c:
    print(b)
