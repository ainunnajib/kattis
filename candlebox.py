import math
d = int(input())
r = int(input())
t = int(input())

x = math.ceil(math.sqrt(2*(r+6)))
y = x - d
while (x*(x+1)//2)-6 + (y*(y+1)//2)-3 != r + t:
    x -= 1
    y -= 1
print(r-((x*(x+1)//2)-6))
