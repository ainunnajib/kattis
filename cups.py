n = int(input())
a = [""] * 2000
for i in range(n):
    s = input().split()
    if s[1].isdigit():
        a[int(s[1])*2] = s[0]
    else:
        a[int(s[0])] = s[1]
for aa in a:
    if aa != "":
        print(aa)