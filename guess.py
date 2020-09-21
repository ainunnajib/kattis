lower = 1
upper = 1000
for _ in range(10):
    guess = (lower+upper)//2
    print(guess)
    ans = input()
    if ans == 'correct':
        break
    elif ans == 'lower':
        upper = guess-1
    elif ans == 'higher':
        lower = guess+1
