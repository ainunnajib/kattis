n = int(input())
l = list(map(int, input().split()))
l.sort()
possible = False
for i in range(len(l)-2):
    if l[i] + l[i+1] > l[i+2]:
        possible = True
        break
print('possible' if possible else 'impossible')
