import sys
N,X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))#리스트로 넣기
for i in arr:
    if i<X:
        print(i, end=' ')