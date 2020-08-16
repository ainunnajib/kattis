a = [ "xxxxxx...xx...xx...xx...xx...xxxxxx", "....x....x....x....x....x....x....x", "xxxxx....x....xxxxxxx....x....xxxxx", "xxxxx....x....xxxxxx....x....xxxxxx", "x...xx...xx...xxxxxx....x....x....x", "xxxxxx....x....xxxxx....x....xxxxxx", "xxxxxx....x....xxxxxx...xx...xxxxxx", "xxxxx....x....x....x....x....x....x", "xxxxxx...xx...xxxxxxx...xx...xxxxxx", "xxxxxx...xx...xxxxxx....x....xxxxxx" ]
plus = ".......x....x..xxxxx..x....x......."
s = []
for i in range(7):
    s.append(input())
l = int(len(s[0]))
n = int((l+1)/6)
x = 0
y = 0
i = 0
while i < n:
    c = ""
    for j in range(7):
        c += s[j][i*6:i*6+5]
    if c == plus:
        i += 1
        break
    x = x*10 + a.index(c)
    i += 1
while i < n:
    c = ""
    for j in range(7):
        c += s[j][i*6:i*6+5]
    y = y*10 + a.index(c)
    i += 1
sum = x+y
result = ["", "", "", "", "", "", ""]
first = True
for c in str(sum):
    digit = a[int(c)]
    for i in range(7):
        if not first:
            result[i] += '.'+digit[5*i:5*i+5]
        else:
            result[i] += digit[5*i:5*i+5]
    first = False
for r in result:
    print(r)