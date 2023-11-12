import sys
sys.setrecursionlimit(10000)

cnt = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and maze[nx][ny] == 1:
                dfs(nx, ny)


for _ in range(cnt):
    
    m, n, bug = map(int, input().split())
    answer = 0
    
    maze = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    
    for _ in range(bug):
        a, b = map(int, input().split())
        maze[b][a] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and maze[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)