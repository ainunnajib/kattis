d2 = {'at':'@', 'to':'2', 'be':'b', 'oh':'o',

      'At':'@', 'To':'2', 'Be':'B', 'Oh':'O'}

d3 = {'and':'&', 'one':'1', 'won':'1', 'too':'2', 'two':'2', 'for':'4',
      'bea':'b', 'bee':'b', 'sea':'c', 'see':'c', 'eye':'i', 'owe':'o',
      'are':'r', 'you':'u', 'why':'y',

      'And':'&', 'One':'1', 'Won':'1', 'Too':'2', 'Two':'2', 'For':'4',
      'Bea':'B', 'Bee':'B', 'Sea':'C', 'See':'C', 'Eye':'I', 'Owe':'O',
      'Are':'R', 'You':'U', 'Why':'Y'}

d4 = {'four':'4', 'Four':'4'}

n = int(input())
for _ in range(n):
    s = list(input())
    ls = len(s)
    i = 0
    while i < ls:
        if i + 4 <= ls:
            x4 = ''.join(s[i:i+4])
            if x4 in d4:
                s[i] = d4[x4]
                s[i+1] = ''
                s[i+2] = ''
                s[i+3] = ''
                i += 4
                continue

        if i + 3 <= ls:
            x3 = ''.join(s[i:i+3])
            if x3 in d3:
                s[i] = d3[x3]
                s[i+1] = ''
                s[i+2] = ''
                i += 3
                continue

        if i + 2 <= ls:
            x2 = ''.join(s[i:i+2])
            if x2 in d2:
                s[i] = d2[x2]
                s[i+1] = ''
                i += 2
                continue

        i += 1

    print(''.join(s))
