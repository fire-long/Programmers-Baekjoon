import sys
H, W = map(int, sys.stdin.readline().rstrip().split())
for i in range(H):
    times = []
    pred = sys.stdin.readline().rstrip()
    time = -1
    for p in pred:
        if p == 'c':
            time = 0
        elif time != -1: #그냥 if하면 계산 고려가 안됨
            time += 1
        times.append(time)
    print(*times, end='\n')