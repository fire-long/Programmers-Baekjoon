import sys
N = int(sys.stdin.readline().rstrip())
res = 5
plus = 7
for i in range(N-1):
    res +=plus
    plus+=3
    res %= 45678
print(res)
#https://star7sss.tistory.com/376

