import sys
N = int(sys.stdin.readline().rstrip())
heights = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

max_height = 0
res = 0
for h in reversed(heights):
    if h > max_height:
        res += 1
        max_height = h
print(res)