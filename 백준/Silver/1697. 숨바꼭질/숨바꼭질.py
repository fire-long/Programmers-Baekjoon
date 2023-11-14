def fastest_time_to_find_brother(N, K):
    visited = [False] * 100001
    queue = [(N, 0)]

    while queue:
        current, time = queue.pop(0)

        if current == K:
            return time

        if 0 <= current * 2 <= 100000 and not visited[current * 2]:
            queue.append((current * 2, time + 1))
            visited[current * 2] = True

        if 0 <= current + 1 <= 100000 and not visited[current + 1]:
            queue.append((current + 1, time + 1))
            visited[current + 1] = True

        if 0 <= current - 1 <= 100000 and not visited[current - 1]:
            queue.append((current - 1, time + 1))
            visited[current - 1] = True

    return -1  # 만약 해답이 안 나오면

# 입력
N, K = map(int, input().split())

# 출력
result = fastest_time_to_find_brother(N, K)
print(result)
