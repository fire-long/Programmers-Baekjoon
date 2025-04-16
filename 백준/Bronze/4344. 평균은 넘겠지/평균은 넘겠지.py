import sys
C = int(sys.stdin.readline().rstrip())
means = []
ratio = []

for i in range(C):
    nums = list(map(int, sys.stdin.readline().split()))
    means.append(sum(nums[1:])/nums[0])
    count = 0
    for j in range(1, nums[0]+1):
        if nums[j]> means[i]:
            count+=1
    ratio.append(count/nums[0]*100)

for r in ratio:
    print("%.3f%%"%r)