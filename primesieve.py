n, q = map(int, input().split())
#converting N to 2*N//6 + N%3 - 1 instead for space optimization
def mini(nn):
    return 2*(nn//6) + nn%3 - 1

isprime = [True] * (n//3+1)
isprime[0] = False #irrelevant bit
for i in range(2,n+1):
    if (i%2 == 0 or i%3 == 0) and i > 3:
        continue
    if i == 2 or i == 3 or isprime[mini(i)]:
        x = i*i
        while x <= n:
            if x%2 != 0 and x%3 != 0:
                isprime[mini(x)] = False
            x += i
print(sum(isprime)+2)
for _ in range(q):
    x = int(input())
    if x == 1:
        print(0)
    elif x == 2 or x == 3:
        print(1)
    elif x%2 == 0 or x%3 == 0:
        print(0)
    else:
        print(int(isprime[mini(x)]))
