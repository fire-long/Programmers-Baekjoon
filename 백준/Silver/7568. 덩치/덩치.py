import sys
N = int(sys.stdin.readline().rstrip())
info = [list(map(int, sys.stdin.readline().rstrip().split())) 
        for _ in range(N)]

for i in range(len(info)):
    big = 0
    for j in range(len(info)):
        if i == j: continue
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            big += 1
    print(big+1, end=" ")