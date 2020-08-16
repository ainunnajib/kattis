n = int(input())
for i in range(n):
    s = input().split()
    name = s[0]
    startdate = s[1]
    birthdate = s[2]
    numcourses = int(s[3])
    eligible = False
    ineligible = False
    petition = False
    if int(startdate[:4]) >= 2010:
        eligible = True
    if int(birthdate[:4]) >= 1991:
        eligible = True
    if not eligible:
        if numcourses > 40:
            ineligible = True
    if not eligible and not ineligible:
        petition = True
    if (eligible):
        print(name + ' eligible')
    elif (ineligible):
        print(name + ' ineligible')
    elif (petition):
        print(name + ' coach petitions')