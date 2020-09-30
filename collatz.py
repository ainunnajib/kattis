a, b = map(int, input().split())
while a + b > 0:
    oria, orib = a, b
    seta = set()
    setb = set()
    lista, listb = [], []

    lista.append(a)
    while a != 1:
        if a%2 == 0:
            a //= 2
        else:
            a = 3*a + 1
        lista.append(a)
    seta = set(lista)

    listb.append(b)
    while b != 1:
        if b%2 == 0:
            b //= 2
        else:
            b = 3*b + 1
        listb.append(b)
    setb = set(listb)

    for i in range(max(len(lista), len(listb))):
        if i < len(lista):
            if lista[i] in setb:
                meet = lista[i]
                break
        if i < len(listb):
            if listb[i] in seta:
                meet = listb[i]
                break

    print(oria, 'needs', lista.index(meet), 'steps,', orib, 'needs', listb.index(meet), 'steps, they meet at', meet)

    a, b = map(int, input().split())
