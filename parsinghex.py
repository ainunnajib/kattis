from sys import stdin

digits = '0123456789abcdef'

for line in stdin.readlines():
    s = line.lower()
    ls = len(s)
    i = 0
    while i < ls:
        while s[i] != '0':
            i += 1
            if i == ls:
                break

        if i < ls - 2:
            if s[i+1] == 'x' and s[i+2] in digits:
                j = i+2
                while s[j] in digits:
                    j += 1
                hex = s[i:j]
                val = 0
                mul = 1
                for c in hex[2:][::-1]:
                    val += digits.index(c) * mul
                    mul *= 16

                print(line[i:j], val)
                i = j + 1
