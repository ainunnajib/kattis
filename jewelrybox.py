import math
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    s = x+y
    m = x*y
    h1 = (s+math.sqrt(s*s-3*m))/6
    h2 = (s-math.sqrt(s*s-3*m))/6
    print(max(h1*(x-2*h1)*(y-2*h1), h2*(x-2*h2)*(y-2*h2)))
