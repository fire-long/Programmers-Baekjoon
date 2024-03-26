import sys
H,M=map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
H += T//60
M += T%60

H += M//60
M %= 60
H %= 24

print(H,M,sep=' ')