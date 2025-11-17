import sys
K, N = map(int, sys.stdin.readline().rstrip().split())
lengths = sorted([int(sys.stdin.readline().rstrip()) for _ in range(K)])

right = max(lengths)
left = 1
result = 0

while left <= right:
    cnt = 0
    mid = (left + right)//2
    
    for l in lengths:
        cnt += l // mid
    if cnt >= N:
        result = mid
        left = mid + 1
    elif cnt < N:
        right = mid - 1
print(result)