n = int(input())
for i in range(n):
    s = input()
    if s == 'P=NP':
        print('skipped')
    else:
        s = s.split('+')
        print(str(int(s[0])+int(s[1])))