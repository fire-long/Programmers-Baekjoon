import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    R, S = sys.stdin.readline().strip().split()
    R = int(R)

    P = ''
    for s in S:
        P += s*R
    print(P)