import sys
for line in sys.stdin.readlines():
    if 'problem' in line.lower():
        print('yes')
    else:
        print('no')
