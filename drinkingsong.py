n = int(input())
s = input()
for i in range(n,1,-1):
    print(str(i) + " bottles of " + s + " on the wall, " + str(i) + " bottles of " + s + ".")
    if i == 2:
        print("Take one down, pass it around, " + str(i-1) + " bottle of " + s + " on the wall.")
    else:
        print("Take one down, pass it around, " + str(i-1) + " bottles of " + s + " on the wall.")
    print("")
print("1 bottle of " + s + " on the wall, 1 bottle of " + s + ".")
print("Take it down, pass it around, no more bottles of " + s + ".")
