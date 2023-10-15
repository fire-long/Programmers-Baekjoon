# 입력 받기
N = int(input())  # 사람의 수
times = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간

# 각 사람이 돈을 인출하는데 필요한 시간을 정렬
times.sort()

# 각 사람이 돈을 인출하는데 필요한 시간의 합 계산
total_time = 0
waiting_time = 0
for time in times:
    waiting_time += time
    total_time += waiting_time

# 결과 출력
print(total_time)