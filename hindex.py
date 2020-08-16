a = []
n = int(input())
for i in range(n):
    k = int(input())
    a.append(k)
a.sort(reverse=True)
num = 0
for i in range(n):
    num += 1
    if a[i] < num:
        break
if num == n and a[n-1] >= n:
    print(n)
else:
    print(num-1)