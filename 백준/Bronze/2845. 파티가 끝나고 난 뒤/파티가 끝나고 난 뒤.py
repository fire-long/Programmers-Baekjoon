import sys
L, P = map(int, sys.stdin.readline().strip().split(' '))
n1, n2, n3, n4, n5 = map(int, sys.stdin.readline().strip().split(' '))
print(n1-L*P, n2-L*P, n3-L*P, n4-L*P, n5-L*P)