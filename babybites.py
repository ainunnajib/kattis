n = int(input())
s = input().split()
ok = True
for i in range(n):
    if s[i] == "mumble":
        continue
    elif int(s[i]) != i+1:
        ok = False
if ok:
    print("makes sense")
else:
    print("something is fishy")
