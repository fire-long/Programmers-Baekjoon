# from itertools import combinations
# import sys
# N, M = map(int, sys.stdin.readline().rstrip().split())
# num = list(range(1, N+1))
# ans = combinations(num, M)
# for i in ans:
#     print(*i)
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
def backTracking(perm):
    if len(perm) == M:
        print(*perm)
        return
    for i in range(1, N+1):
        #조합 문제라서 순서가 중요하지 않음
        if len(perm) > 0 and perm[-1] >= i:
            #기존에 있던 값에 대해서
            #중복된 조합을 막기 위해서
            #마지막 값보다 큰 값에 대해서만 넣을 수 있게 함
            continue
        else:
            perm.append(i)
            backTracking(perm)
            perm.pop()
backTracking([])