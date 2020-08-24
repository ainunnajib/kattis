ref = {"**** ** ** ****":0,
       "  *  *  *  *  *":1,
       "***  *****  ***":2,
       "***  ****  ****":3,
       "* ** ****  *  *":4,
       "****  ***  ****":5,
       "****  **** ****":6,
       "***  *  *  *  *":7,
       "**** ***** ****":8,
       "**** ****  ****":9}
a = []
for _ in range(5):
    s = input()
    a.append( [ s[i*4:i*4+3] for i in range((len(s)+1)//4)] )
n = (len(s)+1)//4
bomb = False
timer = []
for i in range(n):
    digit = ""
    for j in range(5):
        digit += a[j][i]
    if digit in ref:
        timer.append(ref[digit])
    else:
        bomb = True
        break
if bomb:
    print("BOOM!!")
else:
    num = timer[0]
    for i in range(1,len(timer)):
        num *= 10
        num += timer[i]
    if num%6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")
