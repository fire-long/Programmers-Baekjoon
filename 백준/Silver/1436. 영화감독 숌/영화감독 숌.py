import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
result = 666
while True:
    if '666' in str(result):
        cnt += 1
    if cnt == n:
        break
    result += 1
print(result)