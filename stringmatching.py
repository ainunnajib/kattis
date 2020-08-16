while True:
    try:
        p = input()
        t = input()
        ans = []
        i = t.find(p)
        while i != -1:
            ans.append(str(i))
            i = t.find(p, i+1)
        if len(ans) == 0:
            print("")
        else:
            print(" ".join(ans))
    except EOFError:
        pass
