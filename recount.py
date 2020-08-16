from collections import defaultdict
d = defaultdict(int)
s = input()
while s != '***':
    d[s] += 1
    s = input()
maxvotes = max(d.values())
winner = ""
count = 0
for k, v in d.items():
    if v == maxvotes:
        winner = k
        count += 1
if count == 1:
    print(winner)
elif count > 1:
    print("Runoff!")