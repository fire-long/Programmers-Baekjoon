import sys
T = int(sys.stdin.readline())
cases = []
for i in range(T):
    A,B=map(int, sys.stdin.readline().split())
    cases.append(A+B)
    print(f"Case #{i+1}: {cases[i]}")