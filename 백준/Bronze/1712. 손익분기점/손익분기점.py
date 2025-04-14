import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split())

if (C-B) <=0:
    print("-1")
else:
    P = A/(C-B) + 1
    print(int(P))
#https://god-gil.tistory.com/34
#https://yen-world.tistory.com/4