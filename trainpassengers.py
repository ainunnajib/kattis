c, n = map(int, input().split())
train = 0
possible = True
for i in range(n):
    left, enter, stay = map(int, input().split())
    if train < left or train - left + enter > c or (stay > 0 and train - left + enter < c):
        possible = False
    train = train - left + enter
    if i == n-1:
        if train > 0 or stay > 0 or enter > 0:
            possible = False
if possible:
    print("possible")
else:
    print("impossible")
