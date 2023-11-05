# 입력 받기
N, M = map(int, input().split())

# 들어보지도 못한 사람들 명단과 눈으로 본 적도 못한 사람들 명단 받기
not_heard_set = set(input().strip() for _ in range(N))
not_seen_set = set(input().strip() for _ in range(M))

# 듣지도 보지도 못한 사람들 찾기
unheard_unseen_set = not_heard_set.intersection(not_seen_set)

# 정렬 후 출력
unheard_unseen_list = sorted(unheard_unseen_set)
print(len(unheard_unseen_list))
for name in unheard_unseen_list:
    print(name)