s = input()
while s != "0":
    satisfied = True
    k, m = map(int, s.split())
    courses = list(map(int, input().split()))
    for _ in range(m):
        s = list(map(int, input().split()))
        c = s[0]
        r = s[1]
        for course in s[2:]:
            if course in courses:
                r -= 1
        if r > 0:
            satisfied = False
    print("yes" if satisfied else "no")
    s = input()
