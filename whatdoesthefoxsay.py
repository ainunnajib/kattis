n = int(input())
for i in range(n):
    recording = input().split()
    s = input()
    a = []
    while s != 'what does the fox say?':
        s = s.split()
        if s[2] not in a:
            a.append(s[2])
        s = input()
    result = ""
    for w in recording:
        if w not in a:
            if result == "":
                result += w
            else:
                result += " " + w
    print(result)