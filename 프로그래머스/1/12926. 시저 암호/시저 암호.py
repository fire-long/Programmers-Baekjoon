def solution(s, n):
    answer = []
    for x in s:
        if x.isalpha():
            if x.isupper():
                if ord(x)+n > ord('Z'):
                    answer.append(chr((ord(x)+n)-ord('Z')+ord('A')-1)) #65~90
                else:
                    answer.append(chr(ord(x)+n))
            else:
                if ord(x)+n > ord('z'):
                    answer.append(chr((ord(x)+n)-ord('z')+ord('a')-1)) #97~122 
                else:
                    answer.append(chr(ord(x)+n))
        else:
            answer.append(x)
    answer = ''.join(answer)
    return answer