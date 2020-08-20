s = input()
state = [s[0], s[0], s[0]]
flip = [0, 0, 0]
for x in s[1:]:
    for i in range(3):
        if state[i] != x:
            flip[i] += 1
            state[i] = x
    if state[0] != 'U':
        state[0] = 'U'
        flip[0] += 1
    if state[1] != 'D':
        state[1] = 'D'
        flip[1] += 1
print(flip[0])
print(flip[1])
print(flip[2])
