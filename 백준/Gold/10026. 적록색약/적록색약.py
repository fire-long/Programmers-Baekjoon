from collections import deque

def bfs(graph, x, y, is_weakness):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    color = graph[x][y]
    visited[x][y] = True

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            nx, ny = current_x + dx[i], current_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if is_weakness:
                    if color in ['R', 'G']:
                        if graph[nx][ny] in ['R', 'G']:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                    elif graph[nx][ny] == color:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    if graph[nx][ny] == color:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

n = int(input())
graph = [input().strip() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
normal_count = 0
weakness_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i, j, False)
            normal_count += 1

visited = [[False] * n for _ in range(n)] # Reset visited array

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i, j, True)
            weakness_count += 1

print(normal_count, weakness_count)