a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = input()
y = input()
o = ""
for i in range(len(x)):
    if i%2 == 0:
        o += a[(26+a.index(x[i])-a.index(y[i]))%26]
    else:
        o += a[(a.index(x[i])+a.index(y[i]))%26]
print(o)
