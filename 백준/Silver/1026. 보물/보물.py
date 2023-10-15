N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

while len(A) != 0:
    S += max(A) * min(B)
    A.remove(max(A))
    B.remove(min(B))

print(S)