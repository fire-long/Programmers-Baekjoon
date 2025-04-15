#내가 개선한 코드
import sys
N = int(sys.stdin.readline().rstrip())
names = [sys.stdin.readline().rstrip() for _ in range(N)]
for j in range(1, len(names)):
    for i in range(len(names[0])):
        if names[0][i] != names[j][i]:
            names[0] = list(names[0])
            names[0][i] = '?'
            
            #names[0] = names[0].replace(names[0][i],'?')
            #https://www.acmicpc.net/board/view/91661
            
print(''.join(names[0]))