n = int(input())
for _ in range(n):
    k = int(input())
    restaurant = input()
    peasoup = False
    pancake = False
    for __ in range(k):
        menu = input()
        peasoup = peasoup or menu == "pea soup"
        pancake = pancake or menu == "pancakes"
    if peasoup and pancake:
        print(restaurant)
        break
if not (peasoup and pancake):
    print("Anywhere is fine I guess")
