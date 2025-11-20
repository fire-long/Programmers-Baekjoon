def solution(s):
    L = s.split(' ')
    swapped = []
    
    for l in L:
        if len(l) == 0:
            swapped.append(l)        
        elif l[0].isalpha():
            swapped.append(l[0].upper()+l[1:].lower())
        else:
            swapped.append(l[0]+l[1:].lower())
            
    answer = ' '.join(swapped)
    return answer