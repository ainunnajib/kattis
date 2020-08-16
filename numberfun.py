n = int(input())
for i in range(n):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    if a + b == c or a - b == c or b - a == c or a * b == c or c * b == a or c * a == b:
        print("Possible")
    else:
        print("Impossible")