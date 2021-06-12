n, m = map(int, input().split())
fb = [str(i) for i in range(m+1)]
for i in range(3, m+1, 3):
    fb[i] = 'fizz'
for i in range(5, m+1, 5):
    fb[i] = 'buzz'
for i in range(15, m+1, 15):
    fb[i] = 'fizzbuzz'

ans = 1
most = 0
for i in range(1, n+1):
    s = input().split()
    correct = sum([s[j-1] == fb[j] for j in range(1, m+1)])
    if correct > most:
        ans = i
        most = correct
print(ans)