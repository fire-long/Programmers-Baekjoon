import sys
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
# 산성용액: 양수, 알칼리성용액: 음수
# 용액들 중에서 2개를 꼽아 0에 가까운 용액을 오름차순 정렬

left, right = 0, N-1
best = (nums[left], nums[right])

# 정렬 후 투포인터 진행
while left < right:
    s = nums[left] + nums[right]
    if abs(s) < abs(best[0] + best[1]):
        best = (nums[left], nums[right])
    
    if s < 0:
        left += 1
    else:
        right -= 1

print(best[0], best[1])