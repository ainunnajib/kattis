n = int(input())
control = []
strains = []
for _ in range(3):
    strains.append([])
for _ in range(n):
    s = input()
    control.append(s[0] == 'Y')
    strains[0].append(s[1] == 'Y')
    strains[1].append(s[2] == 'Y')
    strains[2].append(s[3] == 'Y')
vaccinated = sum(control)
unvaccinated = n - vaccinated
for v in range(3):
    infectedcontrol = sum([strains[v][i] and not control[i] for i in range(n)])
    infectedvaccinated = sum([strains[v][i] and control[i] for i in range(n)])
    a = infectedvaccinated/vaccinated
    b = infectedcontrol/unvaccinated
    if a >= b:
        print('Not Effective')
    else:
        print((b-a)/b*100)