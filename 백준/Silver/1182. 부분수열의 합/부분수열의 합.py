import sys
N, S = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0


def backTracking(cur, total):
    #cur:현재 부분 집합 개수
    #res:현재까지 전체 합
    global cnt
    if cur == N:
        if total == S:
            cnt+= 1
        return
    backTracking(cur+1, total)#수를 안 더한 경우
    backTracking(cur+1, total+nums[cur])#수를 거꾸로 더해가는 경우

backTracking(0, 0)
print(cnt if S!=0 else cnt-1) #공집합도 합은 0이 되므로, S가 0이면 1을 빼줌
#참고:https://blossom6729.tistory.com/26