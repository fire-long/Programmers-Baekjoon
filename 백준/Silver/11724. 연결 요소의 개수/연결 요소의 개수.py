import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 최대 재귀 깊이 제한 해제

def find_connected_components(n, m, edges):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1

    return count

# 정점의 개수와 간선의 개수 입력 받기
n, m = map(int, input().split())

# 간선 정보 입력 받기
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 연결 요소 개수 찾기 함수 호출 및 결과 출력
print(find_connected_components(n, m, edges))