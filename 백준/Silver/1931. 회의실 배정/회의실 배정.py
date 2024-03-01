#회의의 수 N 입력
N = int(input())

#회의 정보 입력
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))
#끝나는 시간을 기준으로 정렬
meetings.sort(key = lambda x: (x[1], x[0]))

#최대 사용 가능한 회의 수를 저장하는 변수
max_meetings = 0
#이전 회의의 끝나는 시간을 저장하는 변수
prev_end_time = 0

#그리디 알고리즘 적용
for meeting in meetings:
    start, end = meeting
    #현재 회의의 시작시간이 이전 회의의 끝나는 시간보다 크거나 같으면 회의를 선택
    if start >= prev_end_time:
        max_meetings += 1
        prev_end_time = end
#결과 출력
print(max_meetings)