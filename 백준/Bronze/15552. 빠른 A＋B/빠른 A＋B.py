import sys
T = int(sys.stdin.readline())
answers = []
for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    answers.append(A+B)
print(*answers, sep='\n')