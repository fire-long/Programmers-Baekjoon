import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().split()))
total = [0]
tmp = 0

for i in nums:
    tmp += i
    total.append(tmp)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(total[end]-total[start-1])