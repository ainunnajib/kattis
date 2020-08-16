n = int(input())
a = []
while n > 0:
    a.append(n%2)
    n = int(n/2)
l = int(len(a))
x = 1
number = 0
for i in range(l):
    number += int(a.pop()*x)
    x = x*2
print(int(number))