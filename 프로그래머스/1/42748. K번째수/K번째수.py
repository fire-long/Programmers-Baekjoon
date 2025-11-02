def solution(array, commands):
    parts = []
    for c in commands:
        #sort 함수 자체는 return None임
        #-> return 시키려면 sorted() 사용
        part = sorted(array[c[0]-1 : c[1]])
        parts.append(part[c[2]-1])
    answer = parts
    return answer