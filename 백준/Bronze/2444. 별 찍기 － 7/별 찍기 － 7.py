import sys
N = int(sys.stdin.readline())
for i in range(1, 2*N, 1):
    if i <= N:
        print(" "*(N-i), end='')
        print("*"*(2*i-1))
    elif i > N:
        print(" "*(i-N), end='')
        print("*"*(2*(2*N-i)-1))#대칭을 고려