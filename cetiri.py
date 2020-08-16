n = list(map(int, input().split()))
n.sort()
x = n[1]-n[0]
y = n[2]-n[1]
if x == y:
    print(n[2]+x)
elif x > y:
    print(n[0]+y)
elif x < y:
    print(n[1]+x)
