import sys
N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)

scaled = [(score/M*100) for score in scores]
print(sum(scaled)/N)