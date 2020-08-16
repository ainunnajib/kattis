l = input().split()
if l[0] == "0" and l[1] == "0":
    print("Not a moose")
else:
    n = int(max(int(l[0]),int(l[1]))*2)
    if l[0] == l[1]:
        print("Even " + str(n))
    else:
        print("Odd " + str(n))