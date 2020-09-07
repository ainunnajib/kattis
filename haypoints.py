m, n = map(int, input().split())
d = {}
for _ in range(m):
    s = input().split()
    d[s[0]] = int(s[1])

for _ in range(n):
    salary = 0
    s = input()
    while s != '.':
        l = s.split()
        for x in l:
            if x in d:
                salary += d[x]
        s = input()
    print(salary)
