a = int(input())
b = int(input())
x = min(abs(a-b), 360-abs(a-b))
if (360+b-a)%360 != x:
    x *= -1
print(x)
