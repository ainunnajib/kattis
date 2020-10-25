n, m = map(int, input().split())
valid = [True for i in range(2**n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    x = 2**a + 2**b
    for i in range(2**n):
        if x & i == x:
            valid[i] = False
print(sum(valid))
