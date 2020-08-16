line = input().split()
limit = int(line[0])
n = int(line[1])
current = 0
rejected = 0
for i in range(n):
    line = input().split()
    x = int(line[1])
    if line[0] == "enter":
        if current + x > limit:
            rejected += 1
        else:
            current += x
    else:
        current -= x
print(rejected)