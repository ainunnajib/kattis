n = int(input())
for i in range(n):
    s = input()
    if len(s) > 11 and s[:11] == "simon says ":
        print(s[11:])
    else:
        print('')