n = int(input())
d = {}
for _ in range(n):
    s = input().lower()
    s = s.replace('-', ' ').strip()
    d[s] = True
print(len(d))
