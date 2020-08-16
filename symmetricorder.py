set = 0
while True:
    n = int(input())
    if n == 0:
        break
    set += 1
    queue = []
    stack = []
    for i in range(int(n/2)):
        queue.append(input())
        stack.append(input())
    if n%2 == 1:
        queue.append(input())
    print("SET " + str(set))
    while len(queue) > 0:
        print(queue.pop(0))
    while len(stack) > 0:
        print(stack.pop())