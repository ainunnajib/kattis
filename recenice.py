unit = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

numwords = ['' for _ in range(1000)]
for i in range(1, 1000):
    x = i
    hundreds = ''
    if x >= 100:
        hundreds = unit[x//100] + 'hundred'
        x = x%100
    if x < 11:
        numwords[i] = hundreds + unit[x]
    elif x < 20:
        numwords[i] = hundreds + teens[x-10]
    else:
        numwords[i] = hundreds + tens[x//10] + unit[x%10]

lenrest = [i - len(numwords[i]) for i in range(1000)]

n = int(input())
length = 0
l = []
inum = 0
for i in range(n):
    s = input()
    l.append(s)
    if s != '$':
        length += len(s)
    else:
        inum = i

for i in range(1, 1000):
    if lenrest[i] == length:
        l[inum] = numwords[i]
        print(' '.join(l))
        break
