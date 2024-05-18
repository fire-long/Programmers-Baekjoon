#import sys
#S = sys.stdin.readline().strip()
S=input()
li = []
for i in range(ord('a'), ord('z')+1):
    if chr(i) in S:
        li.append(S.index(chr(i)))
    else:
        li.append(-1)
for j in li:
    print(j, end= " ")
#find()를 사용하는 게 보통
#이것도 참고해서 정리하기 https://blog.naver.com/homkim/223150683068
#https://blog.naver.com/summa911/223015799377