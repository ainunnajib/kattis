s = input()
a = 0
b = 0
for i in range(int(len(s)/2)):
    if s[i*2] == "A":
        a += int(s[i*2+1])
    else:
        b += int(s[i*2+1])
if a > b:
    print("A")
else:
    print("B")
