import sys
N = int(sys.stdin.readline().rstrip())
res = 5
plus = 7
for i in range(N-1):
    res +=plus
    plus+=3
print(res%45678)