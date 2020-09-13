n = int(input())
d = {}
valid = True
for i in range(1, n+1):
    s = input().split()
    if s[0] == '->':
        d[s[1]] = True
    else:
        for x in s[:-2]:
            if x not in d:
                valid = False
        if not valid:
            print(i)
            break
        else:
            d[s[-1]] = True
if valid:
    print('correct')
