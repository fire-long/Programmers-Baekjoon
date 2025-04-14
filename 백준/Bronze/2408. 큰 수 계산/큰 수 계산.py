import sys
N = int(sys.stdin.readline().rstrip())
cal = ''
for i in range(2*N-1):
    cal+=(sys.stdin.readline().rstrip())
cal = cal.replace('/', '//')
print(eval(cal))