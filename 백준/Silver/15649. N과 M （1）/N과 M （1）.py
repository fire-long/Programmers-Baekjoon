# from itertools import permutations
# import sys
# N, M = map(int, sys.stdin.readline().rstrip().split())
# num = list(range(1, N+1)) 
# #list() 대신 [] 쓰면 range(1, N+1)로 permutations에 전달됨
# ans = permutations(num, M)
# for i in ans:
#     print(*i)

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
def backTracking(perm):
    if len(perm) == M:
        print(*perm)
        return
    for i in range(1, N+1):
        if i in perm:
            continue
        else:
            #백트래킹의 핵심
            perm.append(i) #push
            backTracking(perm)
            perm.pop() #pull #다른 경로 찾을 수 있게끔
backTracking([])