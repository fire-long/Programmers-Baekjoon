import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
print(N*(M%10))
print(N*((M%100)//10))
print(N*(M//100))
print(N*M)