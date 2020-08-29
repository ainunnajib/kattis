boundx, boundy = map(int, input().split())
windows = []
command = 0
def isin(x, y, w):
    return w[0] <= x and x <= w[2] and w[1] <= y and y <= w[3]

while True:
    try:
        command += 1
        success = False
        s = input().split()
        cmd = s[0]
        if cmd == 'CLOSE':
            x, y = map(int, s[1:])
            for i in range(len(windows)):
                w = windows[i]
                if isin(x, y, w):
                    windows.pop(i)
                    success = True
                    break
            if not success:
                print('Command', str(command)+':', 'CLOSE - no window at given position')
        else:
            x, y, wi, hi = map(int, s[1:])
            if cmd == 'OPEN':
                success = True
                a = x + wi - 1
                b = y + hi - 1
                for w in windows:
                    if isin(x, y, w) or isin(a, b, w) or isin(x, b, w) or isin(a, y, w):
                        success = False
                        break
                    v = [x, y, a, b]
                    if isin(w[0], w[1], v) or isin(w[2], w[3], v) or isin(w[0], w[3], v) or isin(w[2], w[1], v):
                        success = False
                        break
                if success:
                    windows.append([x, y, a, b])
                else:
                    print('Command', str(command)+':', 'OPEN - window does not fit')
            elif cmd == 'RESIZE':
                found = False
                for i in range(len(windows)):
                    w = windows[i]
                    if isin(x, y, w):
                        found = True
                        x = w[0]
                        y = w[1]
                        thewindow = i
                        break
                if not found:
                    print('Command', str(command)+':', 'RESIZE - no window at given position')
                    continue

                success = True
                a = x + wi - 1
                b = y + hi - 1
                for i in range(len(windows)):
                    if i != thewindow:
                        w = windows[i]
                        if isin(x, y, w) or isin(a, b, w) or isin(x, b, w) or isin(a, y, w):
                            success = False
                            break
                        v = [x, y, a, b]
                        if isin(w[0], w[1], v) or isin(w[2], w[3], v) or isin(w[0], w[3], v) or isin(w[2], w[1], v):
                            success = False
                            break

                if success:
                    windows[thewindow][2] = a
                    windows[thewindow][3] = b
                else:
                    print('Command', str(command)+':', 'RESIZE - window does not fit')

            elif cmd == 'MOVE':
                found = False
                for i in range(len(windows)):
                    w = windows[i]
                    if isin(x, y, w):
                        found = True
                        x = w[0]
                        y = w[1]
                        xx = w[2]
                        yy = w[3]
                        thewindow = i
                        break
                if not found:
                    print('Command', str(command)+':', 'MOVE - no window at given position')
                    continue

                if hi == 0: # move horizontally
                    if wi >= 0: # move to right
                        line = [xx, y, xx, yy]
                        while wi > 0:
                            linetry = line.copy()
                            linetry[0] += 1
                            linetry[2] += 1
                            
                            line = linetry
                    else: # move to left
                        linex = x
                elif wi == 0: # move vertically
                    if hi >= 0: # move up
                        pass
                    else: # move down
                        pass




    except EOFError:
        break
print(str(len(windows)), 'window(s):')
for w in windows:
    print(w[0], w[1], w[2]-w[0]+1, w[3]-w[1]+1)
