## alternative answer
#n = int(input())
#s = list(map(int, input().split()))
#o = "1"
#for i in range(n-1):
#    o += (" " + str(s.index(i)+2))
#print(o)

n = int(input())
q = [0] * n
q[0] = 1
s = list(map(int, input().split()))
for i in range(n-1):
    q[s[i]+1] = i+2
print(' '.join(map(str, q)))
