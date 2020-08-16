n = input()
m = input()
div = len(m)-1
if div > len(n):
    n = ('0' * (div-len(n))) + n
r = n[:len(n)-div] + '.' + n[len(n)-div:]
if r[0] == '.':
    r = '0' + r
i = len(r)
while r[i-1] == '0':
    i -= 1
r = r[:i]
if r[len(r)-1] == '.':
    r = r[:len(r)-1]
print(r)