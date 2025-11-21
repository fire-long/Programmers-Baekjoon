def solution(n):
    n = int(n)
    tenary = []
    
    while n != 0:
        tenary.append(n%3)
        n = n//3
    
    answer = int(''.join(map(str, tenary)), 3) #map 함수로 결합할 때 정상 작동
    return answer