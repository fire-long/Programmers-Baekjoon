import sys
from collections import deque
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
blanks = deque()

for row in range(9):
    for col in range(9):
        if graph[row][col] == 0:
            blanks.append((row, col))

def backTracking(cnt):
    global graph #하나의 스도쿠 판에서 하게끔 전역변수 사용

    if cnt == len(blanks):
        #cnt는 인덱스임. 
        #성공적으로 채워진 빈 셀이 몇개인지 추적하는 역할
    
        #재귀를 멈추는 조건문
        #cnt가 빈 공간 개수와 똑같아지면 성공적으로 해결했음을 알 수 있음
        for row in graph:
            print(*row)
        exit(0)
    
    row, col = blanks[cnt]
    
    for i in range(1, 10):
        if check(i, row, col):
            graph[row][col] = i
            backTracking(cnt+1)
            #cnt로 성공적으로 백트래킹을 했기 때문에
            #그 다음 숫자로 재귀적인 호출을 하는 것!
            graph[row][col] = 0

def check(num, row, col):
    #validation, pruning 단계
    #같은 행에 숫자 있는지 확인
    if num in graph[row]:
        return False
    #같은 열에 숫자 있는지 확인
    for row_ in graph:
        if row_[col] == num:
            return False
    
    #3*3 블럭 안에 해당 숫자 있는지 확인
    #스도쿠 문제니까!
    checkRow = (row//3) * 3
    checkCol = (col//3) * 3

    for r in range(checkRow, checkRow+3):
        for c in range(checkCol, checkCol+3):
            if graph[r][c] == num:
                return False
    
    return True

backTracking(0)