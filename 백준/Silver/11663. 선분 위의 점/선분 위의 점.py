import sys
import bisect

N, M = map(int, sys.stdin.readline().split())
coords = sorted(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())

    # start 이상이 처음 나오는 위치
    left = bisect.bisect_left(coords, start)

    # end 초과가 처음 나오는 위치
    right = bisect.bisect_right(coords, end)

    # right는 end 초과 인덱스니까 right - left가 개수
    print(right - left)