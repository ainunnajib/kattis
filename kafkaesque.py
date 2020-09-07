n = int(input())
count, last = 1, 0
for _ in range(n):
    x = int(input())
    if x < last:
        count += 1
    last = x
print(count)
