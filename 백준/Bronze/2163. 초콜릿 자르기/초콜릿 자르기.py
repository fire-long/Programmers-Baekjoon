import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
if N==M:
    print((N**2)-1)
else:
    print(N*M-1)
