import sys
a = list(map(int, sys.stdin.readline().split(' ')))
print((a[0]**2+a[1]**2+a[2]**2+a[3]**2+a[4]**2)%10)
#^ 연산자는 비트 XOR 연산자. 혼동 주의.