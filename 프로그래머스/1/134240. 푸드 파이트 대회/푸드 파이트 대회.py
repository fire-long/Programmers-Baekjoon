def solution(food):
    part = ''
    for i in range(1, len(food)):
        part += f'{i}'*(food[i]//2)
    answer = part+'0'+part[::-1]
    return answer