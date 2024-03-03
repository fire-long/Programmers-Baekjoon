import sys

# 테스트 케이스의 개수 T 입력
T = int(sys.stdin.readline().rstrip())

# 각 테스트 케이스에 대해 실행
for _ in range(T):
    # 지원자의 숫자 N 입력
    N = int(sys.stdin.readline())
    
    # 서류심사 성적과 면접 성적을 저장할 리스트 생성
    applicants = []
    
    # 각 지원자의 서류심사 성적과 면접 성적 입력받아 리스트에 저장
    for _ in range(N):
        document_rank, interview_rank = map(int, sys.stdin.readline().split())
        applicants.append([document_rank, interview_rank])
    applicants.sort()
    
    # 첫 번째 지원자는 서류심사 성적이 가장 좋은 사람이므로 무조건 선발
    selected_count = 1
    
    # 서류심사 성적이 가장 좋은 지원자의 면접 성적을 기준으로 나머지 지원자들과 비교하여 선발 여부 결정
    min_interview_rank = applicants[0][1]
    for i in range(1, N):
        if applicants[i][1] < min_interview_rank:
            # 면접 성적이 더 우수한 경우에만 선발하고 min_interview_rank 갱신
            min_interview_rank = applicants[i][1]
            selected_count += 1

    # 결과 출력
    print(selected_count)