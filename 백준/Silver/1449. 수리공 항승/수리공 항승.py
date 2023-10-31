# Step 1: 입력값 파싱
N, L = map(int, input().split())
leak_locations = list(map(int, input().split()))

# Step 2: 물 누수 위치 리스트를 오름차순으로 정렬
leak_locations.sort()

# Step 3: 변수 초기화
num_tapes = 1
initial_position = leak_locations[0]

# Step 4: 정렬된 물 누수 위치 리스트를 반복
for i in range(1, N):
    # Step 4a: 새 테이프가 필요한지 확인
    if leak_locations[i] > initial_position + L - 1 + 0.5:
        num_tapes += 1
        initial_position = leak_locations[i]
    # Step 4b: 다음 물 누수 위치로 계속

# Step 5: 최종 필요한 테이프 수 출력
print(num_tapes)