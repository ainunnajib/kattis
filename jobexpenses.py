n = int(input())
k = list(map(int, input().split()))
x = 0
for i in k:
    if i<0:
        x -= i
print(x)