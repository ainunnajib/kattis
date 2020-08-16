n = int(input())
tea = list(map(int, input().split()))
m = int(input())
topping = list(map(int, input().split()))
minimum = 1000000
for i in range(n):
    pairs = list(map(int, input().split()))
    for j in range(1, len(pairs)):
        minimum = min(minimum, tea[i]+topping[pairs[j]-1])
cups = int(int(input())/minimum)
if cups > 1:
    print(cups-1)
else:
    print(0)
