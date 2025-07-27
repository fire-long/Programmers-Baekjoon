import sys
A, B = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, B+1):
    for _ in range(i):
        arr.append(i)
print(sum(arr[A-1:B]))