n = int(input())
life_quality = 0.0
for i in range(n):
    s = input().split()
    life_quality += float(s[0])*float(s[1])
print(life_quality)