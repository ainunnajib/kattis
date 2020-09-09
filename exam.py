k = int(input())
a = input()
b = input()
n = len(a)
same, diff = 0, 0
for i in range(n):
    if a[i] == b[i]:
        same += 1
    else:
        diff += 1
print(min(n, min(k, same) + min(n-k, diff)))
