cards = input()
t = 0
g = 0
c = 0
for card in cards:
    if card == 'T':
        t+=1
    elif card == 'G':
        g+=1
    else:
        c+=1
print(t*t+g*g+c*c+7*min(t,g,c))