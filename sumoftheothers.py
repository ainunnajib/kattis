while True:
    try:
        print(sum(map(int, input().split()))//2)
    except EOFError:
        break
