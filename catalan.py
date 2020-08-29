c = [1 for i in range(5001)]
for i in range(2, 5001):
    c[i] = c[i-1]*2*(2*i-1)//(i+1)
q = int(input())
for _ in range(q):
    print(c[int(input())])
