la = list(map(int, input().split()))
na = la[0]
la = la[1:]
lb = list(map(int, input().split()))
nb = lb[0]
lb = lb[1:]

like = [0 for _ in range(1000000)]
for i in la:
    like[i] = 1
for i in lb:
    like[i] += 2

films = 0
last = 0
for i in range(1000000):
    if like[i] == 0:
        continue
    if last in {1, 2} and like[i] == last:
        continue

    last = like[i]
    films += 1

print(films)
