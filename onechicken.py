l = input().split()
n = int(l[0])
m = int(l[1])
if n == m-1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif n < m-1:
    print("Dr. Chaz will have " + str(m-n) + " pieces of chicken left over!")
elif n == m+1:
    print("Dr. Chaz needs 1 more piece of chicken!")
elif n > m+1:
    print("Dr. Chaz needs " + str(n-m) + " more pieces of chicken!")