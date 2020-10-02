import math
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(math.factorial(n)//math.factorial(n-m+1)//math.factorial(m-1))
