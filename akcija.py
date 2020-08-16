n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
total = 0
for i in range(n):
    if i%3 != 2:
        total += a[n-i-1]
print(total)