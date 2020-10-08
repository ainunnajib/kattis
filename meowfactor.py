n = int(input())
ans = 1
for i in range(2, 129):
    if n % (i**9) == 0:
        ans = i
print(ans)
