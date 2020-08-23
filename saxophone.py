d = {'c':[False, True, True, True, False, False, True, True, True, True],
     'd':[False, True, True, True, False, False, True, True, True, False],
     'e':[False, True, True, True, False, False, True, True, False, False],
     'f':[False, True, True, True, False, False, True, False, False, False],
     'g':[False, True, True, True, False, False, False, False, False, False],
     'a':[False, True, True, False, False, False, False, False, False, False],
     'b':[False, True, False, False, False, False, False, False, False, False],
     'C':[False, False, True, False, False, False, False, False, False, False],
     'D':[True, True, True, True, False, False, True, True, True, False],
     'E':[True, True, True, True, False, False, True, True, False, False],
     'F':[True, True, True, True, False, False, True, False, False, False],
     'G':[True, True, True, True, False, False, False, False, False, False],
     'A':[True, True, True, False, False, False, False, False, False, False],
     'B':[True, True, False, False, False, False, False, False, False, False]
     }

n = int(input())
for _ in range(n):
    state = [False] * 10
    presses = [0] * 10
    s = input()
    for x in s:
        nextstate = d[x]
        for i in range(10):
            presses[i] += ((not state[i]) and nextstate[i])
        state = nextstate
    print(' '.join(list(map(str, presses))))
