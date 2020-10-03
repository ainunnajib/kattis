n = int(input())
k = n
digit = 0
while k > 0:
    digit += 1
    k -= 2**digit

n -= (2**digit - 1)
b = bin(n)[2:]
ans = ''
for c in b:
    ans += ('4' if c == '0' else '7')
while len(ans) < digit:
    ans = '4' + ans

print(ans)
