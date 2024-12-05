import sys
import math

input = sys.stdin.readline
n, m = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))
endpoints = list(list(map(int, input().split())) for _ in range(m))

d = dict()

for (x, y) in data:
    g = math.gcd(x, y)
    key = (x // g, y // g)
    if key not in d:
        d[key] = list()
    # (0, 1) (0, 2) (0, 3)과 같이 y축 위의 과일들을 표현하고자 할 때 x좌푯값을 사용하면 안됨.
    d[key].append(abs(x if x != 0 else y))


# 이진 탐색을 위한 사전 정렬
for key in d:
    pts = d[key]
    pts.sort()

answer = 0

for endx, endy in endpoints:
    g = math.gcd(endx, endy)
    key = (endx // g, endy // g)

    if key not in d:
        continue
    pts = d[key] # x좌푯값 or y좌푯값
    end = abs(endx if endx != 0 else endy)

    # 이진 탐색
    left, right = 0, len(pts) - 1
    while left <= right:
        mid = (left + right) // 2
        if pts[mid] <= end:
            left = mid + 1
        else:
            right = mid - 1
    count = right + 1

    answer = max(answer, count)
print(answer)