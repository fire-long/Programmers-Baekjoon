N,M = input().split()
N = int(N)
M = int(M)
result = f'{N+M}\n{N-M}\n{N*M}\n{N//M}\n{N%M}'
print(result)