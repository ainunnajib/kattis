s = input()
l = len(s)
attack = "RBL"
response = "SKH"
r = [] # apparently r = "" with r += "X" hits Time Limit Exceeded
i = 0
while i < l:
    if i < l-2:
        if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
            r.append("C")
            i += 3
            continue
    if s[i] == "R":
        r.append("S")
    elif s[i] == "B":
        r.append("K")
    elif s[i] == "L":
        r.append("H")
    i += 1
print(''.join(r))
