n = int(input())
sour = []
bitter = []
uppersour = 1
upperbitter = 0
for _ in range(n):
    s, b = map(int, input().split())
    uppersour *= s
    upperbitter += b
    sour.append(s)
    bitter.append(b)

mindiff = abs(uppersour) + abs(upperbitter)
for x in range(1, 2**n):
    totals = 1
    totalb = 0
    binary = bin(x)[2:].zfill(n)
    for i in range(n):
        if binary[i] == '1':
            totals *= sour[i]
            totalb += bitter[i]
    mindiff = min(mindiff, abs(totals - totalb))

print(mindiff)
