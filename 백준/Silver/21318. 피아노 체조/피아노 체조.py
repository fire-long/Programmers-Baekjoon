import sys
n = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().rstrip().split()))
q = int(sys.stdin.readline().rstrip())

total = [0 for _ in range(n+1)]
tmp = 0
for i in range(n-1):
    if data[i] > data[i+1]:
        tmp +=1
    total[i+1] = tmp
total[-1] = tmp
for _ in range(q):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(total[y-1]-total[x-1])
