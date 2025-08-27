import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 0 #이미 방문했으니 0 표기

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[False]*N for _ in range(M)]
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        graph[X][Y] = 1
    
    cnt = 0
    for m in range(M):
        for n in range(N):
            if graph[m][n] == 1:
                bfs(graph, m, n)
                cnt += 1
    print(cnt)