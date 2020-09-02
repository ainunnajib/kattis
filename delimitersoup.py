n = int(input())
s = input()
pair = {')':'(', ']':'[', '}':'{'}
stack = []
okay = True
for i in range(n):
    c = s[i]
    if c in ['(', '[', '{']:
        stack.append(c)
    elif c in [')', ']', '}']:
        if len(stack) > 0:
            if stack[-1] == pair[c]:
                stack.pop()
            else:
                print(c, i)
                okay = False
                break
        else:
            print(c, i)
            okay = False
            break
if okay:
    print('ok so far')
