import sys
a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
     'eighteen', 'nineteen', 'twenty']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
d = {}
for i in range(100):
    if i < 21:
        d[i] = a[i]
    elif i%10 == 0:
        d[i] = tens[i//10]
    else:
        d[i] = tens[i//10] + '-' + a[i%10]

while True:
    try:
        s = input().split()
        for i in range(len(s)):
            if s[i].isdigit():
                if i == 0:
                    s[i] = d[int(s[i])].capitalize()
                else:
                    s[i] = d[int(s[i])]
        print(' '.join(s))
    except EOFError:
        break
