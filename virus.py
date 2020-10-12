before = input()
after = input()
lb = len(before)
la = len(after)

i = 0
while before[i] == after[i]:
    i += 1
    if i == la or i == lb:
        break

if i == la or i == lb:
    print(la - i)

else:
    before = before[i:][::-1]
    after = after[i:][::-1]
    lb = len(before)
    la = len(after)

    j = 0
    while before[j] == after[j]:
        j += 1
        if j == la or j == lb:
            break

    print(la - j)
