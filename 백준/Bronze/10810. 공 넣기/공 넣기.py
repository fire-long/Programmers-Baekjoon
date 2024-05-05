import sys
N,M = map(int, sys.stdin.readline().split())
input_list = [0]*N;#0으로 초기화.

for x in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    input_list[i-1:j] = [k]*(j-(i-1))
#for x in range(0,N):
#    print(input_list[x],end=' ')    
print(*input_list)