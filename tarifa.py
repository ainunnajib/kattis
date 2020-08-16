x = int(input())
n = int(input())
result = x * (n+1)
for i in range(n):
    result -= int(input())
print(result)