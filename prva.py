r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))
words = []
for j in range(r):
    s = (''.join(board[j])).split('#')
    for word in s:
        if len(word) > 1:
            words.append(word)
for i in range(c):
    s = ''
    for j in range(r):
        s += board[j][i]
    s = s.split('#')
    for word in s:
        if len(word) > 1:
            words.append(word)
words.sort()
print(words[0])
