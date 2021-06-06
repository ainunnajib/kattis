n = int(input())
total = 0
for _ in range(n):
    total += int(input())
total -= n-1
print(total)