n = int(input())%2
a = input()
b = input()
if n == 0:
    if a == b:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    for i in range(len(a)):
        if a[i:i+1] == b[i:i+1]:
            print('Deletion failed')
            quit()
    print('Deletion succeeded')