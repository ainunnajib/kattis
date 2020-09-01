h, m = map(int, input().split(':'))
s1 = h*60 + m
h, m = map(int, input().split(':'))
s2 = h*60 + m
h, m = map(int, input().split(':'))
p1 = h*60 + m
h, m = map(int, input().split(':'))
p2 = h*60 + m

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
large = 7*24*60 * 24*60

f1 = [False for i in range(large)]
for i in range(large//p1 + 1):
    if s1 + i*p1 < large:
        f1[s1 + i*p1] = True
f2 = [False for i in range(large)]
for i in range(large//p2 + 1):
    if s2 + i*p2 < large:
        f2[s2 + i*p2] = True

never = True
for i in range(large):
    if f1[i] and f2[i]:
        print(days[(i//(24*60))%7])
        h = (i%(24*60))//60
        hh = ('0' if h < 10 else '') + str(h)
        m = i%60
        mm = ('0' if m < 10 else '') + str(m)
        print(hh + ':' + mm)
        never = False
        break
if never:
    print('Never')
