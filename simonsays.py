n = int(input())
for i in range(n):
    s = input()
    if len(s) < 10:
        continue
    if s[:10] == "Simon says":
        print(s[11:])