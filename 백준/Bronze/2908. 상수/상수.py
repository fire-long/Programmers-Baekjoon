import sys
A, B = sys.stdin.readline().strip().split()
AA = int(A[::-1])
BB = int(B[::-1])
if AA>BB:
    print(AA)
    #print(A.reverse()) #이러면 런타임 에러
else:
    print(int(B[::-1]))