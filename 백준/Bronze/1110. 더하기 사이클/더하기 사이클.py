import sys

N = int(sys.stdin.readline().rstrip())
originalN = N
cycleLength = 0

while 1:
    tens = N//10
    units = N%10
    N = units*10 + (tens+units)%10
    cycleLength += 1
    if (N == originalN):
        break
print(cycleLength)
#https://velog.io/@dlzagu/%EB%B0%B1%EC%A4%80-1110%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C