import math
t = int(input())
for _ in range(t):
    n, l, d, g = map(int, input().split())
    d *= g
    area = l**2 * n / (4 * math.tan(math.pi/n))
    area += math.pi * d**2
    area += n * l * d
    print(area)
