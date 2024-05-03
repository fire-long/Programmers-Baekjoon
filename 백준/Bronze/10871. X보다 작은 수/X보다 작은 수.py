import sys
N,X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))#리스트로 넣기
for i in A:
    if i<X:
        print(i, end=' ')