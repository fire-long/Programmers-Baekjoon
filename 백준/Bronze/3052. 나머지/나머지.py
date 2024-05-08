import sys
B = 42
arr = []
for i in range(10):
    A = int(sys.stdin.readline())
    arr.append(A%B)
print(len(set(arr)))