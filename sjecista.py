n = int(input())
r = 0
for i in range(1, n-2):
    r += n * i * (n-2-i)
print(r//4)
