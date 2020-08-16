from collections import defaultdict
x = defaultdict(int)
y = defaultdict(int)
for i in range(3):
    l = input().split()
    x[l[0]] += 1
    y[l[1]] += 1
a = 0
b = 0
for k, v in x.items():
    if v == 1:
        a = k
for k, v in y.items():
    if v == 1:
        b = k
print(str(a) + " " + str(b))