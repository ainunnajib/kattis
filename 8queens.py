from collections import defaultdict
row = defaultdict(int)
col = defaultdict(int)
da = defaultdict(int)
db = defaultdict(int)
count = 0
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == '*':
            row[i] += 1
            col[j] += 1
            da[i+j] += 1
            db[i+7-j] += 1
            count += 1
if max(row.values())*max(col.values())*max(da.values())*max(db.values()) == 1 and count == 8:
    print('valid')
else:
    print('invalid')