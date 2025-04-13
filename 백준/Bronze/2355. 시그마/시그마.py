import sys
A, B = map(int, sys.stdin.readline().strip().split(' '))
print((A+B)*(max(A,B)-min(A,B)+1)//2)