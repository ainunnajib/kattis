r = ["+---+|   ||   |+   +|   ||   |+---+",
     "    +    |    |    +    |    |    +",
     "+---+    |    |+---+|    |    +---+",
     "+---+    |    |+---+    |    |+---+",
     "+   +|   ||   |+---+    |    |    +",
     "+---+|    |    +---+    |    |+---+",
     "+---+|    |    +---+|   ||   |+---+",
     "+---+    |    |    +    |    |    +",
     "+---+|   ||   |+---+|   ||   |+---+",
     "+---+|   ||   |+---+    |    |+---+"]

s = input()
while s != 'end':
    h = s[:2]
    m = s[3:]
    a = int(h[0])
    b = int(h[1])
    c = int(m[0])
    d = int(m[1])
    for i in range(7):
        row = r[a][i*5:(i+1)*5] + '  ' + r[b][i*5:(i+1)*5]
        if i in [2, 4]:
            row += '  o  '
        else:
            row += '     '
        row += r[c][i*5:(i+1)*5] + '  ' + r[d][i*5:(i+1)*5]
        print(row)
    print()
    print()
    s = input()
print('end')