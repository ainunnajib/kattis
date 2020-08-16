n = int(input())
count = 0
for i in range(n):
    s = input()
    if 'CD' not in s:
        count += 1
print(count)