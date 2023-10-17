# 나이트의 이동 가능한 모든 방향 정의
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 나이트의 최소 이동 횟수 계산 함수
def min_moves(board_size, start_x, start_y, end_x, end_y):
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    # 체스판의 각 위치 방문 여부를 기록하기 위한 2차원 리스트. False로 초기화!
    queue = [(start_x, start_y, 0)] #너비우선탐색(BFS) 시, 큐 자료구조를 사용해 구현함.

    while queue:
        # queue가 비어있지 않은 동안에는 계속 반복하는 것을 의미함.
        x, y, moves = queue.pop(0)
        # 큐에서 가장 첨 들어온 원소를 꺼내서 현재 위치('x', 'y')와 그때까지의 이동횟수('moves')로 나눔
        if x == end_x and y == end_y:
            return moves # 현재 위치와 목표 위치가 일치하면 이동횟수 반환 및 함수를 종료함.
        for i in range(8):
            # 나이트의 가능한 8가지 이동 방향에 대해 반복문 실행
            new_x, new_y = x + dx[i], y + dy[i]
            # 현 위치에서 나이트의 한 가지 이동방향('dx[i]', 'dy[i]')으로 이동한 새로운 위치를 계산함.

            # 새로운 위치(new_x, new_y)가 체스판 내에 있고 아직 방문하지 않은 위치인지 확인
            if 0 <= new_x < board_size and 0 <= new_y < board_size and not visited[new_x][new_y]:
                visited[new_x][new_y] = True # 새로운 위치를 방문했음을 표시
                queue.append((new_x, new_y, moves + 1)) 
                # 큐에 새로운 위치와 그 때까지의 이동 횟수를 1 증가시켜서 추가. 
                # 이렇게 함으로써 BFS 알고리즘에서는 최단 경로를 찾을 수 있음.

# 입력 처리 및 결과 출력
test_cases = int(input())
for _ in range(test_cases):
    board_size = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    result = min_moves(board_size, start_x, start_y, end_x, end_y)
    print(result)
