n = int(input())
for i in range(n):
    s = []
    s.append(input())
    s.append(input())
    s.append(input())
    a = [ s[0], s[1], s[2], s[0][0]+s[1][0]+s[2][0], s[0][1]+s[1][1]+s[2][1], s[0][2]+s[1][2]+s[2][2], s[0][0]+s[1][1]+s[2][2], s[0][2]+s[1][1]+s[2][0] ]
    
    xxx = 0
    ooo = 0
    x = 0
    o = 0
    for line in a:
        if line == 'XXX':
            xxx += 1
        elif line == 'OOO':
            ooo += 1
    for line in s:
        for c in line:
            if c == 'X':
                x += 1
            elif c == 'O':
                o += 1
    
    v = True
    
    #Invalid cases
    #two winners
    if xxx > 0 and ooo > 0:
        v = False
    #o has double lines
    if ooo > 1:
        v = False
    #x has double lines
    if xxx > 1:
        v = False
        #except if 2 lines, last move at intersection
        if xxx == 2 and x == 5 and o == 4:
            v = True
    #o starts first (has more)
    if o > x:
        v = False
    #x has too many
    if x > o+1:
        v = False
    #last turn X but O wins
    if x > o and ooo > 0:
        v = False
    #last turn O but X wins
    if x == o and xxx > 0:
        v = False
    
    if (v):
        print('yes')
    else:
        print('no')
    
    if i < n-1:
        s = input()