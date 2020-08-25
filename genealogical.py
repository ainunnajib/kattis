parents = {}
children = {}
births = {}
deaths = {}

def printparents(c, i):
    if c not in parents:
        return

    parent = parents[c]
    for p in parent:
        r = ''
        for _ in range(i):
            r += '  '
        r += p
        if p in births:
            r += ' ' + births[p] + ' -'
            if p in deaths:
                r += ' ' + deaths[p]
        print(r)
        printparents(p, i+1)

def printchildren(p, i):
    if p not in children:
        return

    child = children[p]
    for c in child:
        r = ''
        for _ in range(i):
            r += '  '
        r += c
        if c in births:
            r += ' ' + births[c] + ' -'
            if c in deaths:
                r += ' ' + deaths[c]
        print(r)
        printchildren(c, i+1)

s = input()
printed = False
while s != 'QUIT':
    if s[:5] == 'BIRTH':
        a = s[6:].split(':')
        child = a[0].strip()
        birth = a[1].strip()
        mother = a[2].strip()
        father = a[3].strip()

        births[child] = birth

        parent = [mother, father]
        parent.sort()
        parents[child] = parent

        if mother not in children:
            children[mother] = [child]
        else:
            children[mother].append(child)
            children[mother].sort()

        if father not in children:
            children[father] = [child]
        else:
            children[father].append(child)
            children[father].sort()

    elif s[:5] == 'DEATH':
        a = s[6:].split(':')
        child = a[0].strip()
        death = a[1].strip()

        deaths[child] = death
    elif s[:5] == 'ANCES':
        if printed:
            print()
        printed = True

        person = s[10:]

        print('ANCESTORS of', person)
        printparents(person, 1)

    elif s[:5] == 'DESCE':
        if printed:
            print()
        printed = True

        person = s[12:]

        print('DESCENDANTS of', person)
        printchildren(person, 1)

    s = input()
