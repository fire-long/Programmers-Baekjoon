import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
prefix_sum = [[0]*(m+1) for _ in range(n+1)]


for i in range(1, n+1):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, m+1):
        prefix_sum[i][j] = prefix_sum[i][j - 1] + row[j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1]    

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    part_sum = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    print(part_sum)
  