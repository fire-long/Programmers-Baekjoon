def solution(s, n):
    answer = []
    for x in s:
        if x.isalpha():
            base = ord('A') if x.isupper() else ord('a')
            offset = (ord(x) - base + n) % 26
            answer.append(chr(base + offset))
        else:
            answer.append(x)
    answer = ''.join(answer)
    return answer