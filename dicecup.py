line = input().split()
a = int(line[0])
b = int(line[1])
if a < b:
    a = int(line[1])
    b = int(line[0])
for i in range(b+1, a+2):
    print(i)