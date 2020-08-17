n = int(input())
x = 1
good = True
for _ in range(n):
    i = int(input())
    while x < i:
        print(x)
        x += 1
        good = False
    x += 1
if good:
    print("good job")
