state = []
moves = []
def whowins(left, player):
    if state[left] != -1:
        return (state[left] + player)%2

    if left == 1:
        state[left] = 0
        return player

    for option in moves:
        if option == left:
            state[left] = 0
            return player

        if option < left:
            trywinner = whowins(left-option, 1-player)
            if trywinner == player:
                state[left] = 0
                return player

    state[left] = 1
    return (1-player)

while True:
    try:
        s = list(map(int, input().split()))
        n = s[0]
        state = [-1 for i in range(n+1)]
        m = s[1]
        moves = s[2:]

        for x in range(1, n+1):
            throwaway = whowins(x, 0)

        winner = whowins(n, 0)
        if winner == 0:
            print('Stan wins')
        else:
            print('Ollie wins')
    except EOFError:
        break
