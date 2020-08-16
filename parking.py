s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
t = [ 0 for i in range(100)]
for i in range(3):
    s = input().split()
    start = int(s[0])
    end = int(s[1])
    for j in range(start, end):
        t[j] += 1
total = 0
for x in t:
    if x == 1:
        total += a
    elif x == 2:
        total += b*2
    elif x == 3:
        total += c*3
print(total)