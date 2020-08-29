while True:
    try:
        print(max(1, 2*(int(input())-1)))
    except EOFError:
        break
