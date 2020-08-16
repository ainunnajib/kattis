#To the convention.
#Left beehind.
#Never speak again.
#Undecided.
s = input().split()
while s[0] != '0' or s[1] != '0':
    a = int(s[0])
    b = int(s[1])
    if a+b == 13:
        print('Never speak again.')
    elif a > b:
        print('To the convention.')
    elif a < b:
        print('Left beehind.')
    else:
        print('Undecided.')
    s = input().split()