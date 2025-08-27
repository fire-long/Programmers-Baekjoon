import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [0, 1]
dy = [1, 0]
3
def bfs(x, y):
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x+dx[i]*graph[x][y]
            ny = y+dy[i]*graph[x][y]

            if N <= nx or N <= ny:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == -1:
                return True
            q.append((nx,ny))
    return False

print("HaruHaru" if bfs(0, 0) else "Hing")