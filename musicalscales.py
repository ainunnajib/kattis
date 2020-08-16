def makescale(a, x):
    n = [ 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#' ]
    i = n.index(x)
    a.append(n[i])
    i += 2
    i %= 12
    a.append(n[i])
    i += 2
    i %= 12
    a.append(n[i])
    i += 1
    i %= 12
    a.append(n[i])
    i += 2
    i %= 12
    a.append(n[i])
    i += 2
    i %= 12
    a.append(n[i])
    i += 2
    i %= 12
    a.append(n[i])
    i += 1
    i %= 12
    a.append(n[i])
    return a

n = [ 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#' ]
scales = {}
for x in n:
    a = []
    scales[x] = makescale(a, x)
valid = { x: True for x in n }
m = int(input())
s = input().split()
for c in s:
    for k, v in scales.items():
        if c not in v:
            valid[k] = False
result = ""
for k, v in valid.items():
    if (v):
        if result != "":
            result += ' '
        result += k
if result == "":
    print('none')
else:
    print(result)