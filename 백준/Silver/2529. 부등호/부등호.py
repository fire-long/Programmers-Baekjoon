from itertools import permutations

def check(inequalities, num):
    #부등호 조건 확인
    for i in range(len(inequalities)):
        if inequalities[i] == '<' and num[i] > num[i+1]:
            return False
        if inequalities[i] == '>' and num[i] < num[i+1]:
            return False
    return True

def find_max_min_numbers(k, inequalities):
    max_num = None
    min_num = None
    for perm in permutations('0123456789', k+1):
        #'0123456789' 문자열에서 'k+1'개의 숫자를 가지는 모든 순열을 생성함.
        num = ''.join(perm) #문자열 리스트를 하나의 문자열로 결합함.
        
        if check(inequalities, num):
            if max_num is None or int(num) > int(max_num):
                max_num = num
            if min_num is None or int(num) < int(min_num):
                min_num = num
    return max_num, min_num

# 입력 처리
k = int(input()) #k : 입력으로 들어온 부등호 개수
inequalities = input().split()

# 최댓값과 최솟값 찾기
max_number, min_number = find_max_min_numbers(k, inequalities)

# 결과 출력
print(max_number)
print(min_number)
