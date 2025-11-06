def solution(s):
    answer = True
    
    total = 0
    
    if len(s)%2 == 0 and s.count('(') == s.count(')'):
        for i in s:
            if i == '(':
                total += 1
            elif i == ')':
                total -= 1
            if total < 0:
                answer = False
                break
    else:
        answer = False   

    return answer 