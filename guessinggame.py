lower = 0
upper = 11
dishonest = False
g = int(input())
while g != 0:
    s = input()
    if s == 'too high':
        upper = min(upper, g)
    elif s == 'too low':
        lower = max(lower, g)
    if upper - lower < 2:
        dishonest = True
    if s == 'right on':
        if (dishonest or g >= upper or g <= lower):
            print('Stan is dishonest')
        else:
            print('Stan may be honest')
        lower = 0
        upper = 11
        dishonest = False
    g = int(input())