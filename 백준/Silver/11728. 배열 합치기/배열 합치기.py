import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
A = [0]*N
B = [0]*M

temp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(N):
    A[i] = temp[i]

temp = list(map(int, sys.stdin.readline().rstrip().split()))
for j in range(M):
    B[j] = temp[j]
total = A + B
total.sort(reverse=False)
print(*total)