x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = (x1-x2)**2 + (y1-y2)**2
b = (x1-x3)**2 + (y1-y3)**2
c = (x2-x3)**2 + (y2-y3)**2

if  a == b:
    x = x2 + x3 - x1
    y = y2 + y3 - y1
elif  c == b:
    x = x2 + x1 - x3
    y = y2 + y1 - y3
elif  a == c:
    x = x3 + x1 - x2
    y = y3 + y1 - y2

print(x, y)
