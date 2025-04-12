import sys
total_sec = sum([int(sys.stdin.readline().strip()) for _ in range(4)])
print(total_sec//60)
print(total_sec%60)