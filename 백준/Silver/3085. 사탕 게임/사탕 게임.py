import sys
def count(lst):
    cnt = ans = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            cnt+=1
            ans = max(ans, cnt)
        else:
            cnt=1
    return ans

def solve(arr):
    mx = 0
    for i in range(N-1):
        for j in range(0, N):
            #우측 사탕과 교환
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            mx = max(mx,count(arr[i]))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] #다시 돌리기
            #아래쪽 사탕과 교환
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            mx = max(mx, count(arr[i]), count(arr[i+1]))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

    return mx

N = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline())+[0] for _ in range(N)]+[[0]*(N+1)]
arr_t = list(map(list, zip(*arr)))
ans = max(solve(arr), solve(arr_t))
print(ans)

#참고:https://velog.io/@sh93/%EB%B0%B1%EC%A4%80-3085%EB%B2%88-%EC%82%AC%ED%83%95%EA%B2%8C%EC%9E%84-.-python