n = int(input())
print(str(n) + ":")
for i in range(2, int(n/2)+2):
    if n%(i+i-1) == 0 or (n-i)%(i+i-1) == 0:
        print(str(i) + "," + str(i-1))
    if n%i == 0:
        print(str(i) + "," + str(i))