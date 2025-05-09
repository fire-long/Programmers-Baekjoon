import sys
acceptances = []
def judge(string):
    #첫번째 조건
    if not any(s in 'aeiou' for s in string):
        return False
    
    #두번째 조건:동일 알파벳이 아니라서 모음-모음-모음, 자음-자음-자음이 안됨
    for i in range(len(string)-2):
        #모3
        if (string[i] in 'aeiou') and (string[i+1] in 'aeiou') and (string[i+2] in 'aeiou'):
            return False
        #자3
        if (string[i] not in 'aeiou') and (string[i+1] not in 'aeiou') and(string[i+2] not in 'aeiou'):
            return False

    #세번째 조건
    for i in range(len(string)-1):
        if string[i]==string[i+1] and string[i] not in ['e', 'o']:
            return False
    
    return True


while 1:
    pw = sys.stdin.readline().rstrip()
    if pw == 'end':
        print('\n'.join(acceptances))
        break
    if judge(pw):
        acceptances.append(f'<{pw}> is acceptable.')
    else:
        acceptances.append(f'<{pw}> is not acceptable.')