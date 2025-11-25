def solution(s):
    answer = []
    for idx, ch in enumerate(s):
        prev = s[:idx]
        if ch in prev:
            for i in range(idx-1, -1, -1):
                if prev[i] == ch:
                    answer.append(idx-i)
                    break
        else:
            answer.append(-1)
    return answer