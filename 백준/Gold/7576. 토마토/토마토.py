from collections import deque
import sys

def Graph10():
    def BFS():
        while q:
            x, y = q.popleft()
            for i in range(4):
                ax = x + dx[i]
                by = y + dy[i]
                if 0 <= ax < m and 0 <= by < n and graph[ax][by] == 0:
                    graph[ax][by] = graph[x][y] + 1
                    q.append([ax, by])

    n, m = map(int, input().split())
    graph = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    res = 0

    for i in range(m):
        graph.append(list(map(int, input().split())))

    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                q.append([a, b])

    BFS()

    for a in range(m):
        for b in range(n):
            res = max(res, graph[a][b])
            if graph[a][b] == 0:
                print(-1)
                exit(0)
    print(res - 1)


Graph10()