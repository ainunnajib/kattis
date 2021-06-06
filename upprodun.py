n = int(input())
m = int(input())
for _ in range(m%n):
    print('*' * (m//n+1))
for _ in range(n - m%n):
    print('*' * (m//n))