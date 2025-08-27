#DFS, BFS 모두 가능하나 특정 조건에 따른 탐색을 고려하면 DFS가 더 유용하리라 판단함
#단순 구현도 가능하지만, 알고리즘을 구현하는 연습을 위해 DFS로 작업

def dfs(x, y):
    #바닥 장식이 '-'
    if graph[x][y] == '-':
        graph[x][y]=True
        for _y in [1, -1]:
            #좌우 확인
            Y = y+_y
            #좌우 노드가 범위 내에서 '-' 모양이라면 재귀 함수 호출
            if (Y > 0 and Y < M) and graph[x][Y] == '-':
                dfs(x, Y)

    #바닥 장식이 '|'
    if graph[x][y] == '|':
        graph[x][y]=True
        for _x in [1, -1]:
            #좌우 확인
            X = x+_x
            #좌우 노드가 범위 내에서 '-' 모양이라면 재귀 함수 호출
            if (X > 0 and X < N) and graph[X][y] == '|':
                dfs(X, y)

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
#list() 대신 []를 써서 sys.stdin.readline().rstrip()을 감싸버리면
#'--||' 형태로 저장되어버림.
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            cnt += 1
print(cnt)