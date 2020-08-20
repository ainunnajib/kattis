r = "0123456789ACDEFHJKLMNPRTVWX"
c = [2,4,5,7,8,10,11,13]
d = {'B':'8', 'G':'C', 'I':'1', 'O':'0', 'Q':'0', 'S':'5', 'U':'V', 'Y':'V', 'Z':2}
p = int(input())
for _ in range(p):
    k, s = input().split()
    checksum = 0
    total = 0
    for i in range(8):
        digit = s[i]
        if digit not in r:
            digit = d[digit]
        checksum += c[i] * r.index(digit)
        total += 27**(8-i-1) * r.index(digit)
    if s[8] == r[checksum%27]:
        print(k, total)
    else:
        print(k, "Invalid")
