import sys
import math

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True
def prime_num(M, N):
    pn=[i for i in range(M, N+1) if is_prime(i)]
        
    if not pn:
        #만약 없으면 -1 출력
        print(-1)
    else:
        print(sum(pn))
        print(pn[0])

prime_num(M, N)