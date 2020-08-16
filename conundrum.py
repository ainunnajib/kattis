l = input()
n = int(len(l)/3)
count = 0
for i in range(n):
    if l[i*3] != 'P':
        count += 1
    if l[i*3+1] != 'E':
        count += 1
    if l[i*3+2] != 'R':
        count += 1
print(count)