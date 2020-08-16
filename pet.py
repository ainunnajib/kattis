r = [0, 0, 0, 0, 0]
for i in range(5):
    l = input().split()
    for j in l:
        r[i] += int(j)
print(str(r.index(max(r))+1) + " " + str(max(r)))