def dfs(computer, visited, adj_list):
    visited[computer] = True
    for neighbor in adj_list[computer]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj_list)

# 컴퓨터의 수
n = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(input())

# 그래프를 인접 리스트로 표현
adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 방문 여부를 나타내는 배열
visited = [False] * (n + 1)

# 1번 컴퓨터부터 시작하여 DFS 탐색
dfs(1, visited, adj_list)

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력
print(sum(visited) - 1)