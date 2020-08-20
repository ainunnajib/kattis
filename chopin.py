d = {'A':None, 'A#':'Bb', 'Bb':'A#', 'B':None, 'C':None, 'C#':'Db', 'Db':'C#',
     'D':None, 'D#':'Eb', 'Eb':'D#', 'E':None, 'F':None, 'F#':'Gb', 'Gb':'F#',
     'G':None, 'G#':'Ab', 'Ab':'G#'}
i = 0
while True:
    try:
        i += 1
        s = input().split()
        if d[s[0]] == None:
            print("Case " + str(i) + ": UNIQUE")
        else:
            print("Case " + str(i) + ":", d[s[0]], s[1])
    except EOFError:
        break
