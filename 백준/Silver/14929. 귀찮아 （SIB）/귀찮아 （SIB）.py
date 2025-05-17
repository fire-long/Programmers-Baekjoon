import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))
total = sum(num)
summ=0
for i in range(n):
    summ += num[i]*(total-num[i])
    total -= num[i]
print(summ)

#시간 초과
# total = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         total += num[i] * num[j] 
# print(total)