import sys
N, M = map(int, sys.stdin.readline().split())
basket = [x for x in range(1, N+1)]

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = basket[i-1:j]
    temp.reverse()#reverse 쓰는 게 핵심
    basket[i-1:j] = temp
    
for n in range(N):
    print(basket[n], end=' ')