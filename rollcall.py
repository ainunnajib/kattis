import sys
from collections import defaultdict
names = {}
firstnames = defaultdict(int)
for line in sys.stdin.readlines():
    first, last = line.strip().split()
    if last in names:
        names[last].append(first)
    else:
        names[last] = [first]
    firstnames[first] += 1
for last in sorted(names.keys()):
    for first in sorted(names[last]):
        if firstnames[first] > 1:
            print(first, last)
        else:
            print(first)
