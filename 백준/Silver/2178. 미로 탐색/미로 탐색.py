from collections import deque

def min_spaces_to_pass(N, M, maze):
    queue = deque([(1, 1, 1)])  # (x, y, steps)
    visited = set([(1, 1)])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 오른쪽, 아래, 왼쪽, 위

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == (N, M):
            return steps

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 1 <= new_x <= N and 1 <= new_y <= M and maze[new_x - 1][new_y - 1] == 1 and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, steps + 1))
                visited.add((new_x, new_y))

# 입력값 읽어오기
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# 함수 호출 및 결과 출력
result = min_spaces_to_pass(N, M, maze)
print(result)