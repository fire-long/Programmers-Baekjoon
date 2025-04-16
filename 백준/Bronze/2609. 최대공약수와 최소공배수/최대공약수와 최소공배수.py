import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
def gcd(a, b):
    #최대공약수(gcd)
    if a<b:
        tmp = a
        a = b
        b = tmp
    
    while b!=0:
        n = a%b
        a = b
        b = n
    
    return a
def lcm(a, b):
    #최소공배수(LCM)은 gcd값을 나누는 방식으로 구함
    return (a*b)//gcd(a,b)

print(gcd(A,B))
print(lcm(A,B))

#https://rok93.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-GCD-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98