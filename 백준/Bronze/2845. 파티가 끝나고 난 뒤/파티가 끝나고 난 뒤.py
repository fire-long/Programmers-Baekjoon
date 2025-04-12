import sys
L, P = map(int, sys.stdin.readline().strip().split(' '))
news = list(map(int, sys.stdin.readline().strip().split(' ')))
for i in news:
    print(i - L*P, end=' ')