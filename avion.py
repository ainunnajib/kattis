a = []
for i in range(5):
    if "FBI" in input():
        a.append(str(i+1))
if len(a) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(a))
