import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

cnt = [[0]*M for _ in range(N)]
cnt[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt[nx][ny] = cnt[x][y] + 1
                visited[nx][ny] = True
                q.append([nx, ny])

bfs(0, 0)
print(cnt[N-1][M-1])
