def solution(s):
    cnt = 0
    zeros = 0
    while s != '1':
        # 이진변환
        # 1. 모든 0을 제거
        zeros += s.count('0')
        s = s.replace('0', '')
        # 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿈.
        c = len(s)
        s = bin(c)[2:]
        cnt += 1
    
    answer = [cnt, zeros]
    return answer