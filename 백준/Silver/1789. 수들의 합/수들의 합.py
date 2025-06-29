import sys
S = int(sys.stdin.readline().rstrip())
#가우스의 덧셈알고리즘 문제
i = 0 #1~n까지 더하되, 남은 숫자는 중복되게 됨
#이에 차감하는 방식으로 접근
N = 0

while True:
    if S>i:
        i += 1
        S -= i
        N += 1
    else:
        print(N)
        break

#참고:https://lazypazy.tistory.com/59
#참고:https://konghana01.tistory.com/53