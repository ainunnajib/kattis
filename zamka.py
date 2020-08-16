start = int(input())
end = int(input())
sum = int(input())
for i in range(start, end+1):
    s = str(i)
    k = 0
    for j in s:
        k += int(j)
    if k == sum:
        break
print(i)
for i in range(end,0,-1):
    s = str(i)
    k = 0
    for j in s:
        k += int(j)
    if k == sum:
        break
print(i)