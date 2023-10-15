from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

max_value = -1 
#배열 A가 -100~100이니까, 해당 배열이 최소값이어도 -1로 초기화하면 계산이 됨

for perm in permutations(A):
    total = sum(abs(perm[i] - perm[i + 1]) for i in range(N - 1))
    max_value = max(max_value, total)

print(max_value)