while True:
    try:
        s = input().split()
        domain = {}
        for x in s[1:]:
            domain[x] = 0

        s = input().split()
        codomain = {}
        for y in s[1:]:
            codomain[y] = 0

        n = int(input())
        for _ in range(n):
            s = input().split()
            domain[s[0]] += 1
            codomain[s[2]] += 1

        d = [domain[x] for x in domain]
        c = [codomain[y] for y in codomain]

        minx = min(d)
        maxx = max(d)
        miny = min(c)
        maxy = max(c)

        if maxx > 1: # some domain are mapped more than once
            print('not a function')
        elif miny == 1 and maxy == 1: # all codomain are mapped once and exactly once
            print('bijective')
        elif miny > 0: # all codomain are mapped to
            print('surjective')
        elif maxy <= 1:
            print('injective')
        else:
            print('neither injective nor surjective')
    except EOFError:
        break
