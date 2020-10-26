import math
dkey = {'G major':set([10,0,2,3,5,7,9]),
        'C major':set([3,5,7,8,10,0,2]),
        'Eb major':set([6,8,10,11,1,3,5]),
        'F# minor':set([9,11,0,2,4,5,7]),
        'G minor':set([10,0,1,3,5,6,8])}
notes = ['A','Bb','B','C','C#','D','Eb','E','F','F#','G','Ab']
notesFminor = ['A','Bb','B','C','C#','D','Eb','E','F','F#','G','G#']

n = int(input())
l = []
s = set()
for _ in range(n):
    x = float(input())
    note = round((math.log(x) - math.log(440))/math.log(2)*12)%12
    l.append(note)
    s.add(note)

ans = []
for k in dkey:
    if len(s - dkey[k]) == 0:
        ans.append(k)

if len(ans) != 1:
    print('cannot determine key')
else:
    print(ans[0])
    if ans[0] == 'F# minor':
        for note in l:
            print(notesFminor[note])
    else:
        for note in l:
            print(notes[note])
