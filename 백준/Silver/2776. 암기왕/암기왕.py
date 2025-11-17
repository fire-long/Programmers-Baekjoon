import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    note1 = list(map(int, sys.stdin.readline().rstrip().split()))

    M = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().rstrip().split()))
    note1_set = set(note1)
    for i in range(len(note2)):
        if note2[i] in note1_set:
            print(1)
        else:
            print(0)