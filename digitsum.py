dp = {'':0}
s = 0
for i in range(10):
    s += i
    dp[str(i)] = s
for l in range(1, 15):
    dp['9'*l] = 45 * l * (10**(l-1))

def sumdigitsupto(x):
    if x in dp:
        return dp[x]
    
    ll = len(x) - 1
    if ll > 0:
        f = int(x[0])
        r = 0
        r = sumdigitsupto(x[1:])
        r += (int(x[1:]) + 1) * f
        r += f * dp['9'*ll]
        if f > 0:
            r += 10**ll * dp[str(f-1)]
        dp[x] = r
    return dp[x]

n = int(input())
for _ in range(n):
    a, b = input().split()
    if a != '0':
        a = str(int(a)-1)
    print(sumdigitsupto(b) - sumdigitsupto(a))