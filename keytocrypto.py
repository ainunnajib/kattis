a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
k = input()
r = ""
for i in range(len(s)):
    x = a[(a.index(s[i]) - a.index(k[i]))%26]
    k += x
    r += x
print(r)
