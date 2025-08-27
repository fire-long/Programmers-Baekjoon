from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[] * (N+1) for _ in range(N+1)] ##이 부분 다름

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    graph[n1].append(n2) ##이 부분 다름
    graph[n2].append(n1) ##이 부분 다름

visited1 = [False] * (N+1) #DFS
visited2 = [False] * (N+1) #BFS

## V == start 지점
def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in graph[V]:##range이 아니라 graph[V]에 대해 반복문
            if not visited2[i]: ##조건문은 visited2에 대해서만 존재
                q.append(i)
                visited2[i] = True

def dfs(V):
    visited1[V] = True
    print(V, end=" ")

    for i in graph[V]:##range이 아니라 graph[V]에 대해 반복문
        if not visited1[i]:##조건문은 visited1에 대해서만 존재
            dfs(i)

##정렬 추가
for i in graph:
    i.sort()

dfs(V)
print()
bfs(V)