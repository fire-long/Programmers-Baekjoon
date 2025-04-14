import sys
for _ in range(3):
    res = list(map(int, sys.stdin.readline().rstrip().split()))
    if res.count(0) == 1:
        print("A")
    elif res.count(0) == 2:
        print("B")
    elif res.count(0) == 3:
        print("C")
    elif res.count(0) == 4:
        print("D")
    elif res.count(0) == 0:
        print("E")