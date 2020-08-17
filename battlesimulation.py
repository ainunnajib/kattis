s = input()
l = len(s)
attack = "RBL"
response = "SKH"
r = ""
i = 0
while i < l:
    if i < l-2:
        #if s[i:i+3] in ["RBL", "RLB", "BRL", "BLR", "LRB", "LBR"]: #Time Limit Exceeded
        if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
            r += "C"
            i += 3
            continue
    #r += response[attack.index(s[i])] #Time Limit Exceeded
    if s[i] == "R":
        r += "S"
    elif s[i] == "B":
        r += "K"
    elif s[i] == "L":
        r += "H"
    i += 1
print(r)
