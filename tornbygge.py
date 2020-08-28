n = int(input())
s = list(map(int, input().split()))

count = 1
cur = s[0]
for c in s[1:]:
    if c > cur:
        count += 1
    cur = c
print(count)
