from collections import defaultdict, deque

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            result.append(current)
            stack.extend(sorted(graph[current], reverse=True))

    return result

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            result.append(current)
            queue.extend(sorted(graph[current]))

    return result

def main():
    N, M, V = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for key in graph:
        graph[key].sort()

    dfs_result = dfs(graph, V)
    bfs_result = bfs(graph, V)

    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))

if __name__ == "__main__":
    main()