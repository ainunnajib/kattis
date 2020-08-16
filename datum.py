l = input().split()
d = int(l[0])
m = int(l[1])
a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(m):
    d += a[i]
day = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
print(day[d%7])