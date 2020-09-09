p, t = map(int, input().split())
count = 0
for _ in range(p):
    solved = True
    for __ in range(t):
        s = input()
        a = s[0].lower() + s[1:]
        if a != s.lower():
            solved = False
    count += int(solved)
print(count)
