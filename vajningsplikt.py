turnleft = {'SouthWest':['North', 'East'],
            'EastSouth':['West', 'North'],
            'NorthEast':['South', 'West'],
            'WestNorth':['East', 'South']}
straight = {'SouthNorth':'East',
            'EastWest':'North',
            'NorthSouth':'West',
            'WestEast':'South'}
s = input().split()
a = s[0]+s[1]
b = s[2]
if a in straight:
    if b == straight[a]:
        print('Yes')
    else:
        print('No')
elif a in turnleft:
    if b in turnleft[a]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
