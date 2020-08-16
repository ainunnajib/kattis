s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
x = ""
y = ""
if a + b == c:
    x = "+"
    y = "="
elif a - b == c:
    x = "-"
    y = "="
elif a * b == c:
    x = "*"
    y = "="
elif a / b == c:
    x = "/"
    y = "="
elif a == b + c:
    x = "="
    y = "+"
elif a == b - c:
    x = "="
    y = "-"
elif a == b * c:
    x = "="
    y = "*"
elif a == b / c:
    x = "="
    y = "/"
print(str(a)+x+str(b)+y+str(c))