t = int(input())
for i in range(1, t+1):
    r, p, d = map(int, input().split())
    ingredients = []
    weights = []
    percs = []
    mainingredient = -1
    for j in range(r):
        a = input().split()
        ingredients.append(a[0])
        weights.append(float(a[1]))
        percs.append(float(a[2]))
        if float(a[2]) == 100.0:
            mainingredient = j

    mainweight = weights[mainingredient]

    print("Recipe #", i)
    for j in range(r):
        print(ingredients[j], round(mainweight*d*percs[j]/p/100.0, 1))
    print("----------------------------------------")
