l = input()
f = l[0]
s = set(l)
n = int(input())
for _ in range(n):
    l = input()
    if len(l) < 4:
        continue
    x = set(l)
    if f in x and x.issubset(s):
        print(l)