import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))#리스트로 넣기
v = int(sys.stdin.readline())
print(arr.count(v))