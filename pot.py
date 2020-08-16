n = int(input())
res = 0
for i in range(n):
    s = input()
    x = int(int(s)/10)
    res += x**int(s[len(s)-1])
print(res)