import sys
d = {}
for line in sys.stdin.readlines():
    s = line.split()
    if s[0] == 'def':
        d[s[1]] = int(s[2])
    elif s[0] == 'calc':
        operands = s[3::2]
        operators = s[2::2]
        valid = True
        total = 0
        if s[1] in d:
            total += d[s[1]]
        else:
            valid = False
        for i in range(len(operands)):
            if operands[i] in d:
                if operators[i] == '+':
                    total += d[operands[i]]
                elif operators[i] == '-':
                    total -= d[operands[i]]
            else:
                valid = False
                break
        if valid and total in d.values():
            for k in d:
                if total == d[k]:
                    print(' '.join(s[1:]), k)
                    break
        else:
            print(' '.join(s[1:]), 'unknown')
    elif s[0] == 'clear':
        d = {}
