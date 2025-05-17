import sys
def GCD(a,b):
    #최대공약수
    num = a%b
    if num == 0:
        return b
    else:
        return GCD(b, num)
    #return a if b == 0 else GCD(b, a%b)
#return 빠뜨리면 재귀 호출만 되고 None 반환
def LCM(a,b):
    #최소공배수
    gcd = GCD(a,b)
    return a*b//gcd

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(LCM(a,b))
#참고 : https://blogshine.tistory.com/112
