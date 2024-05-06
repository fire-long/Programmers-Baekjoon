import sys

N,M = map(int, sys.stdin.readline().split())

input_list = [i for i in range(1, N+1)]
temp = 0

for x in range(M):
    i, j= map(int, sys.stdin.readline().split())
    temp = input_list[i-1]
    input_list[i-1] = input_list[j-1]
    input_list[j-1] = temp
    
print(*input_list)