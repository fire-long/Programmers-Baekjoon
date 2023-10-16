# 나이트의 이동 가능한 모든 방향 정의
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 나이트의 최소 이동 횟수 계산 함수
def min_moves(board_size, start_x, start_y, end_x, end_y):
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    queue = [(start_x, start_y, 0)]

    while queue:
        x, y, moves = queue.pop(0)
        if x == end_x and y == end_y:
            return moves
        for i in range(8):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < board_size and 0 <= new_y < board_size and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, moves + 1))

# 입력 처리 및 결과 출력
test_cases = int(input())
for _ in range(test_cases):
    board_size = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    result = min_moves(board_size, start_x, start_y, end_x, end_y)
    print(result)