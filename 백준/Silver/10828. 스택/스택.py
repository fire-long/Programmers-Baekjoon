import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    
    # push
    if cmd[0] == 'push':
        stack.append(cmd[1])
    
    # top
    elif cmd[0] == 'top':
        if len(stack) >= 1:
            top = stack[-1]
        else:
            top = -1
        print(top)
        
    # size
    elif cmd[0] == 'size':
        print(len(stack))
        
    # empty
    elif cmd[0] == 'empty':
        print(1 if len(stack) == 0 else 0)

    # pop
    elif cmd[0] == 'pop':
        if len(stack) >= 1:
            top = stack.pop()
        else:
            top = -1
        print(top)