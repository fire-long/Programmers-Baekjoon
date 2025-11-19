import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
duration = list(map(int, sys.stdin.readline().rstrip().split()))

low = max(duration)
high = sum(duration)
ans = high

def possible(capacity):
    #capacity : 블루레이 용량 후보
    
    # capacity 크기 블루레이로 
    # duration 강의들을 M장 이하로 나눌 수 있나?
    
    #-> 그리디 누적합

    cnt = 1 #블루레이 장 수
    total = 0 #현 블루레이에 담은 강의 길이 합

    for d in duration:
        if total + d > capacity: #현 블루레이에 담으면 넘칠 때
            cnt += 1 #새로운 블루레이 사용
            total = d
        else: #용량이 아직 안 넘치면
            total += d #현 블루레이에 강의 추가
    return cnt <= M

while low <= high:
    mid = (low + high) // 2

    if possible(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)