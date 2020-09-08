n = int(input())
e = 1
x = 1
for i in range(1, n+1):
    x /= i
    e += x
print(e)
