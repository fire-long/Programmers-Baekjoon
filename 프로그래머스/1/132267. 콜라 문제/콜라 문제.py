def solution(a, b, n):
    answer = 0
    while (n//a)*b >= 1:
        new = (n//a)*b
        answer = answer + new
        n = n - (n//a)*a + new
    return answer