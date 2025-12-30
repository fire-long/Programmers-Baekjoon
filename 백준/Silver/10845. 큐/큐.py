import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

queue = deque()
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    
    # push
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    # pop
    elif cmd[0] == 'pop':
        if len(queue) >= 1:
            top = queue.popleft()
        else:
            top = -1
        print(top)
        
    # size
    elif cmd[0] == 'size':
        print(len(queue))
        
    # empty
    elif cmd[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    
    # front
    elif cmd[0] == 'front':
        if len(queue) >= 1:
            print(queue[0])
        else:
            print(-1)    
            
    # back
    elif cmd[0] == 'back':
        if len(queue) >= 1:
            print(queue[-1])
        else:
            print(-1)   