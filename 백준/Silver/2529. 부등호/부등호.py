from itertools import permutations

def check(inequalities, num):
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
        num = ''.join(perm)
        if check(inequalities, num):
            if max_num is None or int(num) > int(max_num):
                max_num = num
            if min_num is None or int(num) < int(min_num):
                min_num = num
    return max_num, min_num

# 입력 처리
k = int(input())
inequalities = input().split()

# 최댓값과 최솟값 찾기
max_number, min_number = find_max_min_numbers(k, inequalities)

# 결과 출력
print(max_number)
print(min_number)