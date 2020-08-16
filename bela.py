l = input().split()
n = int(l[0])
ds = l[1]
dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0
}
notdominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0
}
points = 0
for i in range(4*n):
    l = input()
    if l[1] == ds:
        points += dominant[l[0]]
    else:
        points += notdominant[l[0]]
print(points)