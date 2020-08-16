c = float(input())
n = int(input())
total = 0.0
for i in range(n):
    l = input().split()
    x = float(l[0])
    y = float(l[1])
    total += c*x*y
print(total)